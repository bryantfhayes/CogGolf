main(c,v)char**v;
{
	int r = 0;
	int p = 0;
	for (c=strlen(v[1]);c>=0;c--)
	{
		int m;
		switch(v[1][c])
		{
			case 'I':
				m=1;
				break;
			case 'V':
				m=5;
				break;
			case 'X':
				m=10;
				break;
			case 'L':
				m=50;
				break;
			case 'C':
				m=100;
				break;
			case 'D':
				m=500;
				break;
			case 'M':
				m=1000;
				break;		
		}
		if (!p || p<=m)
			r+=m;
		else
			r-=m;
		p=m;
	}
	printf("%d", r);
}