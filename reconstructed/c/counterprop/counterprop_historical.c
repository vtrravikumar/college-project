/*
 * HISTORICAL SOURCE RECONSTRUCTION
 *
 * Code-02.pdf : COUNTER PROPAGATION implementation
 * Code-03.pdf : continuation
 *
 * Documentary artifact only. Not intended to compile.
 * Source evidence: surviving scanned code PDFs + OCR manuscript.
 */

#include <stdio.h>
#include <float.h>
#include <math.h>
#include <string.h>
#include <dos.h>
#include <process.h>
#include <conio.h>
#include <alloc.h>
#include <stdlib.h>
#include <time.h>
#include <graphics.h>

/* Code-02.pdf : page 20 */

#define no_inputs 10
#define kohonen_nodes 3
#define grossberg_nodes 3
#define no_layers 3
#define n_learn_set 1
#define n_test_set  /* value OCR-uncertain */

union REGS i,o;

struct file_name {
    char f[10];
};

/* Code-02.pdf : page 21 */

int actual_no_inputs;
int file_no,min,tmax,tinc,file_ptr,hundreds,tens,ones;
int i,j,total_no_trials=0,sample_ptr,c;
char buffer[100];

int a1,a2,a3,b1,b2,b3,timetaken,c1,c2,c3;
struct time t1,t2;

int max_n_trails=2000;
int increment=0,learn_ptr=0;
int newline_charum=5;
int no_nodes;

float w1[kohonen_nodes][no_inputs];
float w2[grossberg_nodes][kohonen_nodes];
float x1[no_inputs];
float x2[kohonen_nodes];
float x3[grossberg_nodes];
float desired[grossberg_nodes];

float learning_rate=1.5;
float large=-999.0;
float train_rate_coef=.7,beta=.1;

float x_f[n_learn_set][no_inputs];
float normalizing_factor=1.0;

char *temp;
static char beginning[]="alpha000";
char files[20];

float alpha,largest=-999;
int win_neuron,number=0;
float counter=0.0,count_beta=0.0;

/* FUNCTION DECLARATION */
void test_network(void);
void read_real(void);
void read_weights(void);
void save_weights(void);
void train(void);
void initialize_values(void);
void recalculate_weight_matrix(void);

/* Code-02.pdf : pages 22-24 : MAIN ROUTINE */

main()
int learn_ptr;
int option;
int gd=DETECT,gm;

initgraph(&gd,&gm,"y:\bgi\bgi");
cleardevice();

initialize_values();

option=999;

/*
 * Numeric training-file range:
 *   tmin = 000
 *   tmax = 003
 *   tinc = 1
 *
 * The source constructs names beginning with "alpha000".
 */

tmin=000;
tmax=003;
tinc=1;

i.x.ax=0;
int86(0x33,&i,&o);
i.x.ax=1;
int86(0x33,&i,&o);
i.x.ax=3;
int86(0x33,&i,&o);

while(1)
{
    i.x.ax=3;
    int86(0x33,&i,&o);

    gotoxy(69,24);
    printf("%3d,%3d",o.x.cx,o.x.dx);

    setcolor(6);
    rectangle(3,3,630,470);
    rectangle(4,4,629,469);

    clrscr();

    settextstyle(1,0,2);
    rectangle(70,10,570,80);

    setcolor(9);
    outtextxy(100,30,"COUNTER PROPAGATION NEURAL NETWORK");

    setcolor(7);
    outtextxy(200,120," TRAIN NETWORK ");

    setcolor(8);
    outtextxy(200,170," TEST NETWORK ");

    setcolor(10);
    outtextxy(200,220," READ WEIGHTS ");

    setcolor(11);
    outtextxy(200,270," SAVE WEIGHTS ");

    setcolor(12);
    outtextxy(200,320," QUIT");

    /*
     * The remaining mouse/menu coordinate tests are retained conceptually.
     * Exact punctuation is OCR-uncertain.
     */

    /* TRAIN NETWORK */
    gettime(&t1);
    starttime;

    sample_ptr=0;

    for(file_ptr=tmin;
        file_ptr<=tmax;
        file_ptr=file_ptr+tinc)
    {
        hundreds=file_ptr/100;
        tens=(file_ptr-100*hundreds)/10;
        ones=(file_ptr-100*hundreds-10*tens);

        strcpy(files,beginning);

        files[5]=48+hundreds;
        files[6]=48+tens;
        files[7]=48+ones;

        read_real();
        sample_ptr++;
    }

    printf("\n");
    train();

    gettime(&t2);
    stoptime;

    cleardevice();
    outtextxy(100,10," TRAINING IS OVER ... ");
    outtextxy(100,150," TIME TAKEN : ");

    gotoxy(40,11);
    sprintf(buffer,"%d Sec",timetaken);
    outtextxy(350,150,buffer);

    outtextxy(300,400," PRESS ANY KEY TO CONTINUE...");
    getch();
    cleardevice();

    break;
}

/* Code-03.pdf : pages 1-3 : READ INPUT / CALCULATE OUTPUT */

void read_real(void)
{
    FILE *fdi;
    int found;
    char temp2[80];
    float sum;

    fdi=fopen("alpha000","r");

    /*
     * Source constructs the actual file name in files[]; OCR loses some
     * assignments in this listing.
     */

    printf("\n reading the data. \n");

    j=-1;
    found=999;

    do
    {
        j++;

        if(j%newline_charum==0 && j!=0)
            fscanf(fdi,"\n");

        found=fscanf(fdi,"%f",&x_f[sample_ptr][j]);

    } while(found!=EOF && j<=no_inputs-1);

    actual_no_inputs=j-1;

    for(i=0;i<=actual_no_inputs;i++)
    {
        if(i%5==0)
            printf("\n");

        printf("%f",x_f[sample_ptr][i]);

        if(x_f[sample_ptr][i]==0)
            x_f[sample_ptr][i]=-1;
    }

    fclose(fdi);

    sum=0.0;

    for(i=0;i<=actual_no_inputs;i++)
        sum += x_f[sample_ptr][i]*x_f[sample_ptr][i];

    for(i=0;i<=actual_no_inputs;i++)
        x_f[sample_ptr][i]=x_f[sample_ptr][i]/sqrt(sum);

    /* calculate actual output */
    for(j=0;j<kohonen_nodes;j++)
    {
        sum=0.0;

        for(i=0;i<=no_inputs;i++)
            sum += w1[j][i]*x1[i];

        if(sum>largest)
        {
            largest=sum;
            number=j;
        }

        printf("neuron=%d,sum=%f\n",j,sum);
    }

    for(j=0;j<kohonen_nodes;j++)
        x2[j]=0.0;

    x2[number]=1.0;

    for(j=0;j<grossberg_nodes;j++)
    {
        sum=0.0;

        for(i=0;i<kohonen_nodes;i++)
            sum += w2[j][i]*x2[i];

        x3[j]=sum;
    }
}

/* Code-03.pdf : pages 2-4 : WEIGHT RECALCULATION / TRAINING */

void recalculate_weight_matrix(void)
{
    float sum;

    if(learn_ptr==increment+1)
    {
        counter += 0.0;
        count_beta += 0.0;
    }
    else
    {
        counter += 0.02;
        count_beta += 0.02;
    }

    train_rate_coef=0.7*exp(-counter);

    for(j=0;j<kohonen_nodes;j++)
        for(i=0;i<no_inputs;i++)
        {
            if(j==number)
                w1[j][i]=w1[j][i]+
                    (train_rate_coef*(x1[i]-w1[j][i]));
        }

    sum=0.0;

    for(i=0;i<no_inputs;i++)
        sum += w1[number][i]*w1[number][i];

    if(sum>0.0)
        for(i=0;i<no_inputs;i++)
            w1[number][i]=w1[number][i]/sqrt(sum);

    beta=.1*exp(-count_beta);

    for(j=0;j<grossberg_nodes;j++)
        for(i=0;i<kohonen_nodes;i++)
            if(i==number)
                w2[j][i]=w2[j][i]+
                    (beta*(desired[j]-w2[j][i]));

    increment=learn_ptr;
}

void initialize_values(void)
{
    float sum;

    srand(2);

    for(j=0;j<kohonen_nodes;j++)
        for(i=0;i<no_inputs;i++)
            w1[j][i]=(rand()/32767.0-.5)*1.0;

    srand(2);

    for(j=0;j<grossberg_nodes;j++)
        for(i=0;i<kohonen_nodes;i++)
            w2[j][i]=(rand()/32767.0-.5)*1.0;

    sum=0.0;

    for(j=0;j<kohonen_nodes;j++)
        for(i=0;i<no_inputs;i++)
            sum += w1[j][i]*w1[j][i];

    for(j=0;j<kohonen_nodes;j++)
        for(i=0;i<no_inputs;i++)
            w1[j][i]=w1[j][i]/sqrt(sum);

    sum=0.0;

    for(j=0;j<grossberg_nodes;j++)
        for(i=0;i<kohonen_nodes;i++)
            sum += w2[j][i]*w2[j][i];

    for(j=0;j<grossberg_nodes;j++)
        for(i=0;i<kohonen_nodes;i++)
            w2[j][i]=w2[j][i]/sqrt(sum);

    for(i=0;i<grossberg_nodes;i++)
        desired[i]=0.0;
}

void train(void)
{
    int total_no_trials;

    while(train_rate_coef>0.01)
    {
        for(learn_ptr=0;
            learn_ptr<n_learn_set;
            learn_ptr++)
        {
            desired[learn_ptr]=1.0;

            for(i=0;i<no_inputs;i++)
                x1[i]=x_f[learn_ptr][i];

            /* calculate actual output */
            recalculate_weight_matrix();
        }
    }
}

/* Code-03.pdf : pages 4-5 : TEST NETWORK */

void test_network(void)
{
    int test_ptr;
    FILE *fdi;
    int found;
    float sum;
    char test_file[20];

    cleardevice();

    for(test_ptr=0;test_ptr<n_test_set;test_ptr++)
    {
        settextstyle(1,0,1);
        outtextxy(100,42," PLEASE ENTER THE TEST FILE NAME: ");

        gotoxy(60,4);
        scanf("%s",&test_file);

        fdi=fopen(test_file,"r");

        /*
         * The source reads a test vector, converts zero values to -1,
         * normalizes it, and then calls the network output calculation.
         */
    }
}

/* Code-03.pdf : pages 6-8 : READ/SAVE WEIGHTS */

void read_weights(void)
{
    static char weightf[]="weights.wts";
    FILE *fdi;
    int i,j;
    float sum;

    clrscr();
    cleardevice();

    fdi=fopen(weightf,"r");

    printf("reading file==>%s\n",weightf);
    getch();

    if(fdi==NULL)
    {
        printf("could not open input file!\n");
        printf("press any key to continue.");
        return;
    }

    printf("\nreading the weights....\n");

    for(i=0;i<kohonen_nodes;i++)
        for(j=0;j<no_inputs;j++)
        {
            fscanf(fdi,"%f",&w1[i][j]);
            printf("%f\t",w1[i][j]);
        }

    printf("\n");

    for(i=0;i<grossberg_nodes;i++)
        for(j=0;j<kohonen_nodes;j++)
        {
            fscanf(fdi,"%f",&w2[i][j]);
            printf("%f\t",w2[i][j]);
        }

    printf("\n");

    fclose(fdi);

    outtextxy(300,400," PRESS ANY KEY TO CONTINUE...");
    getch();
}

void save_weights(void)
{
    static char weightf[]="weights.wts";
    FILE *fdi;
    int i,j;

    clrscr();
    cleardevice();

    fdi=fopen(weightf,"w");

    sprintf(buffer,"SAVING FILE ==> %s\n",weightf);
    outtextxy(200,100,buffer);

    if(fdi==NULL)
    {
        printf("could not open output file\n");
        printf("press any key to continue.");
        return;
    }

    outtextxy(200,250,"SAVING THE WEIGHTS...");

    for(i=0;i<kohonen_nodes;i++)
        for(j=0;j<no_inputs;j++)
            fprintf(fdi,"%f\t",w1[i][j]);

    for(i=0;i<grossberg_nodes;i++)
        for(j=0;j<kohonen_nodes;j++)
            fprintf(fdi,"%f\t",w2[i][j]);

    fclose(fdi);

    outtextxy(300,400," PRESS ANY KEY TO CONTINUE...");
    getch();
}

/*
 * HISTORICAL RECONSTRUCTION NOTE
 *
 * The source uses DOS graphics, mouse interrupts and file-based training
 * data. OCR damage is substantial in places. This file therefore preserves
 * the identifiable program structure while marking/refraining from filling
 * algorithmically uncertain sections.
 *
 * It is not evidence of a particular historical C compiler.
 */
