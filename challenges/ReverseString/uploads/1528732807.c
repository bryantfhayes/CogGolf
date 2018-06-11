main(c, v)char**v;
{
	while(c++<99)
		for(char* z = v[1];*z; c^*z++ ? 0 : putchar(c));
}