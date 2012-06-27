#!/bin/sh
p=nrd
svn=http://$p.googlecode.com/svn/trunk

revno=$1
specfile=nagios-$p.spec

set -e
svn co $svn${revno:+@$revno} $p
svnrev=$(svnversion $p)

d=$p-r$svnrev
rm -rf $d
svn export $p $d

# write inc/*
cd $d
perl Makefile.PL
cd -

tar -cjf $d.tar.bz2 --exclude-vcs $d
../dropin $d.tar.bz2

sed -i -e "
	s/^\(%define[ \t]\+svnrev[ \t]\+\)[0-9]\+\$/\1$svnrev/
" $specfile
../md5 $specfile
