/*
 * HISTORICAL SOURCE RECONSTRUCTION
 *
 * Project:
 *   ANALYSIS OF ARTIFICIAL NEURAL NETWORK
 *   USING BACK PROPAGATION & GENETIC ALGORITHM
 *
 * Source:
 *   Code-01.pdf, pages 1-24
 *   OCR manuscript: archive/manuscripts/manuscript-full-run-111-pages.md
 *
 * STATUS:
 *   Historical/documentary reconstruction.
 *   NOT intended to compile.
 *
 * IMPORTANT:
 *   OCR-derived uncertainty is deliberately preserved in comments.
 *   Where the scan must be consulted to establish an exact token,
 *   the uncertainty is marked rather than silently repaired.
 */

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 1
 * ------------------------------------------------------------------------- */

/* PROGRAM TO TRAIN AND TEST NEURAL NETWORK USING
   GENETIC ALGORITHM */

/* INCLUDING OF HEADER FILES */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <alloc.h>
#include <dos.h>
#include <time.h>
#include <float.h>
#include <conio.h>
#include <graphics.h>

/* DEFINITION OF GA PARAMETERS */
#define MAXPOP 50
#define MAXSTR 100
#define CHROMLEN 10
#define MAX 10
#define NODE0 2
#define NODE1 2
#define NODE2 2
#define NODE3 1
#define NCLS 4
#define CONCN 10
#define MERR .20
#define thres 0.2

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 2
 * ------------------------------------------------------------------------- */

/* DEFINITION FOR TIMING CALCULATION */
#define starttime
/* OCR/source listing shows the following assignments around the macro. */
a1 = t1.ti_hour;
a2 = t1.ti_min;
a3 = t1.ti_sec;

#define stoptime
b1 = t2.ti_hour;
b2 = t2.ti_min;
b3 = t2.ti_sec;

c1 = (b1-a1);
c2 = (b2-a2);
c3 = (b3-a3);
c = (((c1*60)+c2)*60+c3);
timetaken = c;

/* INITIALISE REGISTER */
union REGS i,o;

/* DEFINE THE STRUCTURES */
typedef struct {
    int allele;
} gene;

typedef gene chromosome[MAXSTR];

typedef struct {
    chromosome chrom;
    long double x;
    double fitness;
    int parent1, parent2, site;
    int count;
} individual;

typedef individual population[MAXPOP];

/* VARIABLES DECLARATION */
population oldpop,newpop;
int popsize,lchrom,gen,maxgen;

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 3
 * ------------------------------------------------------------------------- */

double pcross, pmutation;
double sumfitness;
int mutation, ncross;
double fmax, avg, fmin;
int no_of_sol, MIN;
double oldrand[55];
int jrand, y, store;

float se;
float hwgt1[MAX][MAX], hwgt2[MAX][MAX];
float layer2[MAX][MAX];
float owgt[MAX][MAX], layer1[MAX][MAX], out[MAX][MAX];
int x[MAX][MAX], desire[MAX][MAX];
double finar[20];
float pas[CONCN];
float ee[CONCN];
int gbit[CONCN];
float lrange, urange;
int bb, range;

int a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4;
int c,timetaken;
struct time t1,t2;

population top;

char infile[] = "in.dat";
char outfile[] = "out.dat";
char wtfile[] = "wt.dat";

FILE *ptin;
FILE *ptout;
FILE *ptfwt;
FILE *ptfwti;
FILE *ptgbit;
FILE *ptres;
FILE *ptpop;
FILE *ptval;
char buffer[100];

/* FUNCTION DECLARATIONS */
double garandom();
void randomise();
int garand(int,int);
void warmup_rand(double);
void adv_rand();
gene flip(double probability);
void initialise();
void initreport();
void initpop();
void initdata();
double objectfn(chromosome);
long double decode(chromosome chrom,int lbits);
int success();
void getpheno(int *x, chromosome chrom, int lchrom);
void writechrom(chromosome, int);
int search(long double,int);
int form_cur_pop();
void report(int);
void encode(int,int);
void pause(void);
void generation();
void crossover(chromosome,chromosome,chromosome,chromosome,
               int*,int*,int*,int*,double*,double*);
int select(int,double,population);
gene mutation(gene,double,int*);
void statistics(int,double*,double*,double*,double*,individual*);
void forward(int);
void ftest(void);
void get_iputs(void);
void get_oputs(void);
void finalweights(float pas[CONCN]);
void storeweights(population);
float calcerror(int);
int menu(void);

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 4-7
 * MAIN ROUTINE
 * ------------------------------------------------------------------------- */

main()
int i,j,f,count=0;
int ch,mfit;
float temp;
double temp1;
int gd=DETECT, gm;
population storepop;

initgraph(&gd,&gm,"y:\bgi\bgi");

f=0;
cleardevice();

if((ptres=fopen("result.dat","w"))==NULL)
    printf("\n Cannot open result.dat");
fclose(ptres);

if((ptpop=fopen("xpop.dat","w"))==NULL)
    printf("\n Cannot open xpop.dat");
fclose(ptpop);

if((ptgbit=fopen("xgranbit.dat","w"))==NULL)
    printf("\n Cannot open xgranbit.dat");
fclose(ptgbit);

if((ptval=fopen("value.dat","r"))==NULL)
    printf("\n Cannot open value.dat");
fclose(ptval);

get_iputs();
get_oputs();
cleardevice();
pause();

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

    gotoxy(65,24);
    printf("%3d,%3d",o.x.cx,o.x.dx);

    setcolor(14);
    settextstyle(1,0,2);
    rectangle(70,20,550,65);
    rectangle(2,2,635,470);
    rectangle(3,3,634,469);

    setcolor(2);
    outtextxy(150,41,"GENETIC ALGORITHM IN NEURAL NETWORK");

    setcolor(3);
    outtextxy(200,200," TRAIN NETWORK ");

    setcolor(5);
    outtextxy(200,260," TEST NETWORK ");

    setcolor(4);
    outtextxy(200,320," QUIT");

    /*
     * The remainder of the menu and mouse-coordinate tests are retained
     * conceptually from the listing; exact OCR punctuation is uncertain.
     */

    /* FINAL TESTING */
    /*
    gotoxy(2,2);
    printf("\nFINAL TESTING.....\n");
    ftest();

    fprintf(ptres,"\n");
    for(i=0;i<NCLS;i++)
        for(j=0;j<NODE3;j++)
            fprintf(ptres,"out[%d][%d]=%f",i,j,out[i][j]);

    sprintf(buffer,"TESTING OVER...");
    outtextxy(200,320,buffer);
    getch();
    cleardevice();
    pause();
    */

    /*
     * TRAIN NETWORK
     */
    initialise();

    for(i=0;i<popsize;i++)
        storepop[i]=oldpop[i];

    for(i=0;i<popsize;i++)
        for(j=0;j<lchrom;j++)
            fprintf(ptpop,"%d",oldpop[i].chrom[j].allele);

    rewind(ptgbit);
    rewind(ptres);

    {
        int b=0;
        while(b<1)
            b++;

        gen=0;
        count++;

        for(i=0;i<popsize;i++)
            oldpop[i]=storepop[i];

        for(i=0;i<CONCN;i++)
            fscanf(ptgbit,"%d",&gbit[i]);

        for(i=0;i<popsize;i++)
            oldpop[i].fitness=objectfn(oldpop[i].chrom);

        statistics(popsize,&fmax,&avg,&fmin,&sumfitness,newpop);

        gettime(&t1);
        starttime;

        do
        {
            printf("..");
            delay(100);

            gen++;
            generation();

            statistics(popsize,&fmax,&avg,&fmin,&sumfitness,newpop);

            for(i=0;i<MAXPOP;i++)
                oldpop[i]=newpop[i];

            no_of_sol=form_cur_pop();
            success();

            if((gen%100)==0)
                pause();

        } while(gen<maxgen);

        gettime(&t2);
        stoptime;

        fcloseall();
        storeweights(oldpop);

        printf("\nTIME TAKEN %d SECS",timetaken);
        printf("\nTRAINING IS OVER");
        getch();
        pause();
    }

    break;
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 8
 * ROUTINE TO PERFORM GENERATION OF GA CYCLE
 * ------------------------------------------------------------------------- */

generation()
int i,j,cross,mate1,mate2;
population temppop;

j=0;
mate1=select(popsize,sumfitness,oldpop);
mate2=select(popsize,sumfitness,oldpop);

crossover(oldpop[mate1].chrom,oldpop[mate2].chrom,
          newpop[j].chrom,newpop[j+1].chrom,
          &ncross,&lchrom,&mutation,&jcross,
          &pcross,&pmutation);

newpop[j].x=decode(newpop[j].chrom,lchrom);
newpop[j].fitness=objectfn(newpop[j].chrom);
newpop[j].parent1=mate1;
newpop[j].parent2=mate2;
newpop[j].site=jcross;

newpop[j+1].x=decode(newpop[j+1].chrom,lchrom);
newpop[j+1].fitness=objectfn(newpop[j+1].chrom);
newpop[j+1].parent1=mate1;
newpop[j+1].parent2=mate2;
newpop[j+1].site=jcross;

/*
 * OCR/source-page uncertainty remains around the temporary population
 * replacement and store-index logic.
 */

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 9
 * ROUTINE TO EVALUATE OBJECTIVE FUNCTION
 * ------------------------------------------------------------------------- */

double objectfn(chromosome n1)
int i,j,k,l,m,n,c,p,ct;
individual a[CONCN];
individual d[CONCN];
float b[20];
float in=0.0;

i=0;
k=0;
l=0;
m=0;
c=0;
p=0;
n=0;

/*
 * The scan/OCR shows the chromosome being divided into CHROMLEN-bit
 * sections, each decoded to a weight value.
 */
for(j=0,m=0;j<lchrom;j++)
{
    if(j==m)
    {
        for(i=m;i<j+CHROMLEN;i++)
            d[n].chrom[k++].allele=n1.chrom[i].allele;

        b[p]=decode(d[n].chrom,CHROMLEN);
        m=m+CHROMLEN;
        p++;
        n=0;
        l=0;
    }
}

for(p=0;p<CONCN;p++)
{
    ee[p]=b[p]/100.00;

    if(ee[p]>urange)
        ee[p]=urange-ee[p];
}

k=0;
p=0;
l=0;
m=0;
i=0;
se=0.0;

finalweights(ee);

for(i=0;i<NCLS;i++)
    forward(i);

in=calcerror(i);
se=se+in;
se=se/(NODE3*NCLS);

pause();
return(se);

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 10
 * ROUTINE TO PERFORM DECODING OF BINARY STRING TO AN INTEGER
 * ------------------------------------------------------------------------- */

long double decode(chromosome chrom,int lbits)
int i,j;
long double accum=0.0,powerof2=1.0;

for(i=0;i<lbits;i++)
    ;

for(i=lbits-1;i>=0;i--)
{
    if(chrom[i].allele)
        accum+=powerof2;

    powerof2*=2.0;
}

return accum;

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 11-12
 * INITIALISATION OF GA PARAMETERS / POPULATION
 * ------------------------------------------------------------------------- */

initdata()
char ch;
int j;
float temp;

ptval=fopen("value.dat","r");

fscanf(ptval,"%d",&popsize);
fscanf(ptval,"%d",&maxgen);
fscanf(ptval,"%Lf",&pcross);
fscanf(ptval,"%lf",&pmutation);
fscanf(ptval,"%f",&lrange);
fscanf(ptval,"%f",&urange);

getch();
cleardevice();

randomise();
mutation=0;
ncross=0;
lchrom=CHROMLEN*CONCN;

temp=2*urange*100;
range=(int)temp;

fprintf(ptres,"popsize %d,gen %d,cp %.21f,mp %.21f,range(%.21f,%.21f)\n",
        popsize,maxgen,pcross,pmutation,lrange,urange);

fclose(ptval);

initpop()
int i,j,l;
int y;
long double temp=0.0;

for(j=0;j<popsize;j++)
{
    bb=0;

    for(i=0;i<CONCN;i++)
    {
        printf(".");
        delay(100);
    }

    y=random(range);
    encode(j,y);

    for(i=0;i<lchrom;i++)
        temp=decode(oldpop[j].chrom,lchrom);

    oldpop[j].x=temp/120;
    oldpop[j].parent1=0;
    oldpop[j].parent2=0;
    oldpop[j].site=0;
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 12
 * ROUTINE TO PERFORM ENCODING OF AN INTEGER TO BINARY STRING
 * ------------------------------------------------------------------------- */

void encode(int index,int value)
{
    int i,j,term;
    chromosome t1;
    long int y;

    /*
     * OCR listing continues into the random-number implementation.
     * Exact statements are scan-dependent and are intentionally not
     * invented here.
     */
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 13-14
 * RANDOM NUMBER GENERATION / BIT FLIPPING / ROULETTE SELECTION
 * ------------------------------------------------------------------------- */

double garandom()
{
    jrand++;

    if(jrand>54)
        jrand=0;

    adv_rand();

    return(oldrand[jrand]/2);
}

int garand(int low,int high)
{
    int i;

    if(low>-high)
        i=low;
    else
        i=(int)(2*garandom()*(high-low+1)+low);

    if(i>high)
        i=high;

    return i;
}

randomise()
double seed;

do
    seed=0.45678;
while(seed<0.0 || seed>1.0);

warmup_rand(seed);

gene flip(double probability)
gene tmp;

if(probability==1.0)
    tmp.allele=1;
else
    tmp.allele=((2*garandom())<=probability);

return tmp;

int select(int popsize,double sumfitness,population pop)
double rand,partsum;
int j;
double temp;

j=-1;
partsum=0.0;
rand=0.0;
temp=0.0;

temp=garandom();
rand=temp*sumfitness;

do
{
    j++;
    partsum += pop[j].fitness;
}
while(!(partsum>=rand) && (j==(popsize-1)));

return j;

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 15-16
 * MUTATION / CROSSOVER
 * ------------------------------------------------------------------------- */

gene mutation(gene allval,double mutation,int *nmutation)
{
    gene mutate;
    gene tmp;

    mutate=flip(pmutation);

    if(mutate.allele)
    {
        (*nmutation)++;
        tmp.allele=(!allval.allele);
        return tmp;
    }

    return allval;
}

crossover(chromosome p1,chromosome p2,chromosome c1,chromosome c2,
          int *ncross,int *lchrom,int *nmutation,int *jcross,
          double *pcross,double *pmutation)
int j;

if(flip(*pcross).allele)
{
    *jcross=garand(0,(*lchrom)-1);
    (*ncross)++;
}
else
    *jcross=(*lchrom)-1;

for(j=0;j<*jcross;j++)
{
    c1[j]=mutation(p1[j],*pmutation,nmutation);
    c2[j]=mutation(p2[j],*pmutation,nmutation);
}

/*
 * The remaining tail of the crossover listing is visibly damaged by OCR.
 * The surviving intent is a one-point crossover followed by mutation.
 */

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 16-18
 * POPULATION SEARCH / SUCCESS / STATISTICS
 * ------------------------------------------------------------------------- */

writechrom(chromosome chrom,int lchrom)
{
    int j;

    for(j=0;j<lchrom;j++)
        ;
}

int search(long double pheno,int no_of_sol)
{
    long double temp=0.0;
    population curpop;
    int i,j;

    for(j=0;j<no_of_sol;j++)
    {
        temp=fabs(pheno-curpop[j].x);

        if(fabs(pheno-curpop[j].x)<=1e-25)
            return j;
    }

    return -1;
}

int form_cur_pop()
{
    int i,place,k;
    int no_of_sol=1;
    population curpop;

    /*
     * The listing groups offspring having equal phenotype values and
     * maintains a count for each distinct solution.
     *
     * Exact array indices are OCR-uncertain and should be checked against
     * Code-01.pdf page 17 before publication.
     */
    return no_of_sol;
}

int success()
{
    int i,j;
    double min;

    MIN=0;
    min=oldpop[0].fitness;

    for(i=1;i<popsize;i++)
    {
        if(oldpop[i].fitness<min)
            min=oldpop[i].fitness;
    }

    if(min<0.05)
        return 1;

    return 0;
}

statistics(int popsize,double *max,double *avg,double *min,
           double *sumfitness,individual *pop)
{
    int i;
    float temp=0.0;

    *sumfitness=0.0;
    *avg=0.0;
    *max=0.0;
    *min=0.0;

    for(i=0;i<popsize;i++)
        *sumfitness += pop[i].fitness;

    *avg=*sumfitness/popsize;
    *max=*min=pop[0].fitness;

    for(i=1;i<popsize;i++)
    {
        if(pop[i].fitness>*max)
            *max=pop[i].fitness;

        if(pop[i].fitness<*min)
            *min=pop[i].fitness;
    }
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 19
 * FORWARD PROPAGATION
 * ------------------------------------------------------------------------- */

void forward(int count)
{
    int i,j;
    float net1,net2,net3;

    for(i=0;i<NODE1;i++)
    {
        net1=0.0;

        for(j=0;j<NODE0;j++)
            net1 += hwgt1[j][i] * x[count][j];

        layer1[count][i]=1/(1+exp(-net1));
    }

    for(i=0;i<NODE2;i++)
    {
        net2=0.0;

        for(j=0;j<NODE1;j++)
            net2 += hwgt2[j][i] * layer1[count][j];

        layer2[count][i]=1/(1+exp(-net2));
    }

    for(i=0;i<NODE3;i++)
    {
        net3=0.0;

        for(j=0;j<NODE2;j++)
            net3 += owgt[j][i] * layer2[count][j];

        out[count][i]=1/(1+exp(-net3));
    }

    pause();
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : page 20
 * ROUTINE TO CALCULATE FINAL WEIGHTS
 * ------------------------------------------------------------------------- */

void finalweights(float pas[CONCN])
{
    int i,j,k,kk;

    k=0;
    kk=0;

    for(i=0;i<NODE0;i++)
        for(j=0;j<NODE1;j++)
        {
            if(gbit[kk]==0)
                hwgt1[i][j]=0;
            else
                hwgt1[i][j]=pas[k]*gbit[kk];

            k++;
            kk++;
        }

    for(i=0;i<NODE1;i++)
        for(j=0;j<NODE2;j++)
        {
            if(gbit[kk]==0)
                hwgt2[i][j]=0;
            else
                hwgt2[i][j]=pas[k]*gbit[kk];

            k++;
            kk++;
        }

    for(i=0;i<NODE2;i++)
        for(j=0;j<NODE3;j++)
        {
            if(gbit[kk]==0)
                owgt[i][j]=0;
            else
                owgt[i][j]=pas[k]*gbit[kk];

            k++;
            kk++;
        }
}

/* -------------------------------------------------------------------------
 * Code-01.pdf : pages 22-24
 * STORING FINAL WEIGHTS / TESTING
 * ------------------------------------------------------------------------- */

void storeweights(population pop)
{
    int i,j,k,l,m,n,c,p;
    individual a[CONCN];
    individual d[CONCN];
    float b[CONCN];
    float e[CONCN];

    /*
     * Historical listing decodes CHROMLEN-bit chunks and writes the
     * resulting weights to the weight file.
     */
    for(p=0;p<CONCN;p++)
    {
        e[p]=b[p]/100.00;

        if(e[p]>urange)
            e[p]=urange-e[p];
    }

    /*
     * The source then writes:
     *   NODE0 x NODE1 weights
     *   NODE1 x NODE2 weights
     *   NODE2 x NODE3 weights
     * to the final weight file.
     *
     * Exact OCR-damaged file-handle spelling is deliberately not repaired.
     */
}

/*
 * ftest()
 *
 * The surviving listing loads the final weights, reads the test patterns,
 * performs forward propagation for NCLS patterns, and asks the operator
 * for the number of patterns identified before calculating a percentage
 * of success.
 *
 * Source: Code-01.pdf pages 23-24.
 */

/* -------------------------------------------------------------------------
 * Historical reconstruction note
 * -------------------------------------------------------------------------
 *
 * This file intentionally remains a documentary artifact.
 *
 * Several statements above have been normalized only where the OCR clearly
 * represents a standard C token and the surrounding source evidence makes
 * the intent unambiguous (for example #include <stdio.h>, array brackets,
 * and simple loop punctuation).
 *
 * Algorithmically meaningful uncertainty is explicitly retained.
 *
 * The companion modern implementation must be treated as a separate
 * reconstruction and must not be presented as the original 1998 program.
 */
