#!/usr/local/bin/perl

print "Enter a string: ";

my $str = <>; # read string



chomp($str);

my $rev = reverse($str);

if ($str eq $rev)
{
    print "The input string is a palindrome!\n";
}
else
{
    print "The input string is not a palindrome.\n";
}
