main(c, v)char**v;
{
	for (c = strlen(v[1]); c--;)
		putchar(v[1][c]);
}