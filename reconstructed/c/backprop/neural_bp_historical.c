/*
 * HISTORICAL SOURCE RECONSTRUCTION
 *
 * Code-02.pdf : BACKPROPAGATION implementation
 *
 * Documentary artifact only. Not intended to compile.
 * Source evidence: scanned code PDF + OCR manuscript.
 *
 * OCR uncertainty is preserved rather than silently repaired.
 */

/* Code-02.pdf : pages 4-5 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <alloc.h>
#include <dos.h>
#include <time.h>
#include <conio.h>
#include <graphics.h>

/* DEFINITION OF BACKPROPAGATION PARAMETERS */
#define ncls 4
#define node0 2
#define node1 2
#define node2 2
#define node3 1
#define thresb 0.5
#define MAX1 30
#define ALPHA 1
#define MITER 5000

/* TIMING CALCULATION */
#define starttime
ab1=t1.ti_hour;
ab2=t1.ti_min;
ab3=t1.ti_sec;

#define stoptime
bb1=t2.ti_hour;
bb2=t2.ti_min;
bb3=t2.ti_sec;
bc1=(bb1-ab1);
bc2=(bb2-ab2);
bc3=(bb3-ab3);
bc=(((bc1*60)+bc2)*60+bc3);
btimetaken=bc;

/* VARIABLES */
union REGS i,o;

int desire[MAX1][MAX1];
int bx[MAX1][MAX1];

float layerb1[MAX1][MAX1],layerb2[MAX1][MAX1],outb[MAX1][MAX1];
float hwgtb1[MAX1][MAX1],hwgtb2[MAX1][MAX1];
float owgtb[MAX1][MAX1];
float obwgt[MAX1];
float hbwgt1[MAX1],hbwgt2[MAX1];

float finerr;
struct time bt1,bt2;

char infile[]="in.dat";
char outfile[]="out.dat";
char wgtfile[]="wgt.dat";

int ab1,ab2,ab3,ab4,bb1,bb2,bb3,bb4;
int bc1,bc2,bc3,bc4;
int bc,btimetaken,choose;

FILE *ptiwt;
FILE *pttwt;
FILE *ptfwtb1;
FILE *ptin1;
FILE *ptout1;
FILE *pterr;
FILE *ptmse;
FILE *ptop;
FILE *ptresb;

/* FUNCTION DECLARATIONS */
void initweights(void);
void forward1(int count);
void reverse(int count);
void tempweights(void);
void prevweights(void);
void finalweights(void);
void get_ip(void);
void get_op(void);
void test(void);
float calcerror1(int count);
void pause1(void);
int menu1(void);
float randomweight(unsigned init);

/* Code-02.pdf : pages 6-8 : MAIN ROUTINE */

main()
int i,j,k,l,m;
int s[5];
int ch;
float sqerr;
float msgerr;
int epoc=1;
int gd=DETECT,gm;

initgraph(&gd,&gm,"y:\bgi\bgi");
cleardevice();

if((pterr=fopen("oserr.dat","w+"))==NULL)
    printf("\n Cannot open oserr.dat");

if((ptop=fopen("osop.dat","w+"))==NULL)
    printf("\n Cannot open osop.dat");

if((ptmse=fopen("osmse.dat","w+"))==NULL)
    printf("\n Cannot open osmse.dat");

if((ptresb=fopen("result.dat","a"))==NULL)
    printf("\n Cannot open result.dat");

rewind(pterr);
rewind(ptop);
rewind(ptmse);

cleardevice();

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

    gotoxy(69,25);
    printf("%3d,%3d",o.x.cx,o.x.dx);

    settextstyle(1,0,2);
    setcolor(7);
    rectangle(3,3,635,470);
    rectangle(4,4,634,469);
    rectangle(70,10,570,80);

    outtextxy(100,30,"BACK-PROPAGATION NEURAL NETWORK");

    setcolor(2);
    outtextxy(200,200," TRAIN NETWORK ");

    setcolor(4);
    outtextxy(200,260," TEST NETWORK ");

    setcolor(3);
    outtextxy(200,320," QUIT");

    /*
     * Mouse/menu selection logic is retained only where the OCR is clear.
     * The original listing uses int86(0x33) and graphics functions.
     */

    srand(12345);
    initweights();
    get_ip();
    get_op();

    outtextxy(10,10," TRAINING ..");
    gotoxy(10,10);

    msgerr=1.0;

    gettime(&bt1);
    starttime;

    while(MITER >= epoc)
    {
        sqerr=0.0;
        epoc++;

        for(i=1;i<=ncls;i++)
            forward1(i);

        for(i=1;i<=ncls;i++)
        {
            reverse(i);
            sqerr=sqerr+finerr;
        }

        msgerr=sqerr/(node3*ncls);

        printf(".");
        delay(30);

        if((epoc % 50) != 0)
            ;
        else
            fprintf(ptmse,
                    "\n epoc = %d, sqerror = %f, msqerror = %f",
                    epoc,sqerr,msgerr);

        if((epoc % 2000)==0)
            tempweights();
    }

    gettime(&bt2);
    stoptime;

    finalweights();

    printf("\n Final Weights stored");

    fclose(pterr);
    fclose(ptmse);
    fclose(ptresb);

    ptresb=fopen("result.dat","w");
    fprintf(ptresb,"%d",btimetaken);

    printf("\n Time Taken %d Secs",btimetaken);
    printf("\nTraining is over..\n");
    getch();
    cleardevice();

    break;
}

/* Code-02.pdf : page 8-9 : FORWARD PROPAGATION */

void forward1(int count)
{
    int i,j;
    float net1,net2,net3;

    for(i=1;i<=node1;i++)
    {
        net1=0.0;

        for(j=1;j<=node0;j++)
            net1 += hwgtb1[j][i]*bx[count][j];

        net1 += hbwgt1[i];

        layerb1[count][i]=1/(1+exp(-net1));
    }

    for(i=1;i<=node2;i++)
    {
        net2=0.0;

        for(j=1;j<=node1;j++)
            net2 += hwgtb2[j][i]*layerb1[count][j];

        net2 += hbwgt2[i];

        layerb2[count][i]=1/(1+exp(-net2));
    }

    for(i=1;i<=node3;i++)
    {
        net3=0.0;

        for(j=1;j<=node2;j++)
            net3 += owgtb[j][i]*layerb2[count][j];

        net3 += obwgt[i];

        outb[count][i]=1/(1+exp(-net3));
    }

    return;
}

/* Code-02.pdf : pages 9-11 : REVERSE PROPAGATION */

void reverse(int count)
int i,j,k;
float delta[MAX1][MAX1];
float delta1[MAX1][MAX1],delta2[MAX1][MAX1];
float sum[MAX1];
float temp=0.0;
float temp1=0.0;

for(i=1,finerr=0.0;i<=node3;i++)
{
    temp=outb[count][i]*(1-outb[count][i]);
    temp1=desire[count][i]-outb[count][i];

    delta[count][i]=temp*temp1;
    finerr += 0.5*temp1*temp1;
}

for(k=1;k<=node2;k++)
{
    sum[k]=0.0;

    for(i=1;i<=node3;i++)
        sum[k] += owgtb[k][i]*delta[count][i];

    temp=layerb2[count][k]*(1-layerb2[count][k]);
    delta2[count][k]=temp*sum[k];
}

for(k=1;k<=node1;k++)
{
    sum[k]=0.0;

    for(i=1;i<=node2;i++)
        sum[k] += hwgtb2[k][i]*delta2[count][i];

    temp=layerb1[count][k]*(1-layerb1[count][k]);
    delta1[count][k]=temp*sum[k];
}

for(j=1;j<=node3;j++)
    for(i=1;i<=node2;i++)
    {
        temp=delta[count][j]*layerb2[count][i];
        owgtb[i][j]=owgtb[i][j]+ALPHA*temp;
    }

for(j=1;j<=node2;j++)
    for(i=1;i<=node1;i++)
    {
        temp=delta2[count][j]*layerb1[count][i];
        hwgtb2[i][j]=hwgtb2[i][j]+ALPHA*temp;
    }

for(i=1;i<=node1;i++)
{
    for(j=1;j<=node0;j++)
    {
        temp=delta1[count][i]*bx[count][j];
        hwgtb1[i][j]=hwgtb1[i][j]+ALPHA*temp;
    }
}

return;

/* Code-02.pdf : pages 11-14 : WEIGHT FILE ROUTINES */

void tempweights(void)
{
    int i,j;

    if((pttwt=fopen("ostwt.dat","w+"))==NULL)
    {
        printf("\n Cannot open ostwt.dat file");
        exit(0);
    }

    rewind(pttwt);

    for(i=1;i<=node0;i++)
        for(j=1;j<=node1;j++)
            fprintf(pttwt,"%f",hwgtb1[i][j]);

    for(i=1;i<=node1;i++)
        fprintf(pttwt,"%f",hbwgt1[i]);

    for(i=1;i<=node1;i++)
        for(j=1;j<=node2;j++)
            fprintf(pttwt,"%f",hwgtb2[i][j]);

    for(i=1;i<=node2;i++)
        fprintf(pttwt,"%f",hbwgt2[i]);

    for(i=1;i<=node2;i++)
        for(j=1;j<=node3;j++)
            fprintf(pttwt,"%f",owgtb[i][j]);

    for(i=1;i<=node3;i++)
        fprintf(pttwt,"%f",obwgt[i]);

    fclose(pttwt);
}

void finalweights(void)
{
    int i,j;

    if((ptfwtb1=fopen(wgtfile,"w+"))==NULL)
    {
        printf("\nCannot open weight file");
        exit(0);
    }

    rewind(ptfwtb1);

    for(i=1;i<=node0;i++)
        for(j=1;j<=node1;j++)
            fprintf(ptfwtb1,"%f\n",hwgtb1[i][j]);

    for(i=1;i<=node1;i++)
        fprintf(ptfwtb1,"%f\n",hbwgt1[i]);

    for(i=1;i<=node1;i++)
        for(j=1;j<=node2;j++)
            fprintf(ptfwtb1,"%f\n",hwgtb2[i][j]);

    for(i=1;i<=node2;i++)
        fprintf(ptfwtb1,"%f\n",hbwgt2[i]);

    for(i=1;i<=node2;i++)
        for(j=1;j<=node3;j++)
            fprintf(ptfwtb1,"%f\n",owgtb[i][j]);

    for(i=1;i<=node3;i++)
        fprintf(ptfwtb1,"%f\n",obwgt[i]);

    fclose(ptfwtb1);
}

/* Code-02.pdf : pages 13-14 : INITIAL WEIGHTS */

float randomweight(unsigned init)
{
    int num;

    if(init==1)
        srand((unsigned)time(NULL));

    num=rand()%100;

    return 2*((float)(num/100.0))-1;
}

void initweights(void)
{
    int i,j;

    if((ptiwt=fopen("osiwt.dat","w+"))==NULL)
        printf("\nCannot open weight file");

    for(i=1;i<=node0;i++)
        for(j=1;j<=node1;j++)
        {
            hwgtb1[i][j]=randomweight(0);
            fprintf(ptiwt,"%f\n",hwgtb1[i][j]);
        }

    for(i=1;i<=node1;i++)
    {
        hbwgt1[i]=fabs(randomweight(0));
        fprintf(ptiwt,"%f\n",hbwgt1[i]);
    }

    for(i=1;i<=node1;i++)
        for(j=1;j<=node2;j++)
        {
            hwgtb2[i][j]=randomweight(0);
            fprintf(ptiwt,"%f\n",hwgtb2[i][j]);
        }

    for(i=1;i<=node2;i++)
    {
        hbwgt2[i]=fabs(randomweight(0));
        fprintf(ptiwt,"%f\n",hbwgt2[i]);
    }

    for(i=1;i<=node2;i++)
        for(j=1;j<=node3;j++)
        {
            owgtb[i][j]=randomweight(0);
            fprintf(ptiwt,"%f\n",owgtb[i][j]);
        }

    for(i=1;i<=node3;i++)
    {
        obwgt[i]=fabs(randomweight(0));
        fprintf(ptiwt,"%f\n",obwgt[i]);
    }

    fclose(ptiwt);
}

/* Code-02.pdf : pages 15-19 : TESTING / ERROR / INPUT */

void test(void)
{
    int n,p,in,v,i,j,k,l;
    float percent;
    int s;
    float store[MAX1];
    float array[MAX1][MAX1];
    float finer[MAX1];
    float large;
    float temp;

    /*
     * The source loads wgt.dat, reads NCLS patterns, calls forward1(),
     * asks for the number of patterns identified, and calculates:
     *
     * percent = (float)in/(float)ncls*100.00;
     *
     * Exact file-variable spellings are OCR-uncertain.
     */
}

void pause1(void)
{
    getch();
}

float calcerror1(int count)
{
    int i;
    float errorterm;
    float merrorterm=0.0;
    float ferrorterm;

    for(i=1;i<=node3;i++)
    {
        errorterm=desire[count][i]-outb[count][i];
        merrorterm += errorterm*errorterm;
    }

    ferrorterm=0.5*merrorterm;
    return ferrorterm;
}

void get_ip(void)
{
    int i,j;
    int s;

    if((ptin1=fopen(infile,"r"))==NULL)
        printf("\nCannot open input file");

    rewind(ptin1);

    for(i=1;i<=ncls;i++)
        for(j=1;j<=node0;j++)
        {
            fscanf(ptin1,"%d",&s);

            if(s==0)
                bx[i][j]=0;
            else
                bx[i][j]=1;
        }

    fclose(ptin1);
}

void get_op(void)
{
    int i,j;
    int s;

    if((ptout1=fopen(outfile,"r"))==NULL)
        printf("\nCannot open output file");

    rewind(ptout1);

    for(i=1;i<=ncls;i++)
        for(j=1;j<=node3;j++)
        {
            fscanf(ptout1,"%d",&s);

            if(s==0)
                desire[i][j]=0;
            else
                desire[i][j]=1;
        }

    fclose(ptout1);
}

/*
 * prevweights() is present in the source listing and reads an earlier
 * weight file. The OCR of its declarations/file name is uncertain.
 *
 * Source: Code-02.pdf pages 18-19.
 *
 * void prevweights(void) { ... }
 */

/*
 * HISTORICAL RECONSTRUCTION NOTE
 *
 * This file is a documentary transcription/reconstruction, not a modern
 * implementation. Some syntactic normalization was necessary to make the
 * extracted listing readable (for example obvious OCR substitutions in
 * standard #include directives). Algorithmically meaningful uncertainty is
 * explicitly marked.
 *
 * Do not use this file as evidence that the original compiler was Watcom C.
 */
