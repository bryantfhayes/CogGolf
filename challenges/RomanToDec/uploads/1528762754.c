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
    {
        if (n[*s] >= n[*(s+1)])
            c+=n[*s];
        else
        {
            c+=n[*(s+1)] - n[*s];
            s++;
        }
    }
    
    printf("%d", c);
}