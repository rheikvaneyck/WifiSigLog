BEGIN {
	c=0
}
/Cell [0-9]+/{
	c=c+1
	addr=$5
	cmd="date +'%F %T'"
	cmd|getline timestamp;
	close(cmd)
}
/ESSID/{
	split($0, l, ":")
	gsub("\"","",l[2])
	essid=l[2]
}
/Signal level/{
	split($3, s,"=")
	split(s[2],ss,"/")
	sig=ss[1]/ss[2]
	line[c]=sprintf("%s;%s;%s;%s",timestamp,addr,essid,sig)
}
END {
	for(i=1;i<=c;i++)
		print line[i]
}
