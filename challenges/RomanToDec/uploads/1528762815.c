int n [78];

int main(c, v)char** v;
{
    n[77] = 1000;
    n[68] = 500;
    n[67] = 100;
    n[76] = 50;
    n[88] = 10;
    n[86] = 5;
    n[73] = 1;
    char* s = v[1];
    
    for(c=0; *s; s++)
        c += n[*s] >= n[*(s+1)] ? n[*s] : -n[*s];
    
    printf("%d", c);
}