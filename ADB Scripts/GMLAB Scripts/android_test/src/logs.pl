#/************************************************************************
# * Copyright (C) 1998-2016 Connected Devices, Innominds Software Pvt Ltd.
# *
# * This file is part of Connected Devices Project
# *
# * Connected Devices Project and associated code can not be copied
# * and/or distributed without a written permission of
# * Innominds Software Pvt Ltd., and/or it subsidiaries
# *
# * Description: This module script called when smoketest invokes the
#                btcheck.
#* For any modification contact @Ramamohan (rbandapalli@innominds.com)
#************************************************************************/
use strict;
use warnings;

my $DevID=$ARGV[0];

&adbLogging();
&kernaLogging();
&radioLogging();
&eventsLogging();
&topLogging();
&lsofLogging();
&dumpsysMeminfo();
&procrank();

sub adbLogging
    {
     
       system " start \"UIlogs-$DevID\" cmd /c \"adb -s $DevID logcat -v threadtime > UIlogs.txt\"";
}
sub kernaLogging 
   {
      system " start \"kernellogs-$DevID\" cmd /c \"adb -s $DevID shell cat /proc/kmsg -v time > kernellogs.txt\"";
}

sub radioLogging
   {
      system " start \"Radiologs-$DevID\" cmd /c \"adb -s $DevID logcat -b radio -v time  > radiologs.txt\"";
}

sub eventsLogging 
   {
      system " start \"Events-$DevID\" cmd /c \"adb -s $DevID logcat -b events -v time  > events.txt\"";
}
sub topLogging
{
system " start \"Toplogs-$DevID\" cmd /c \"adb -s $DevID shell top > top.txt\"";
}
sub lsofLogging
{
system " start \"LSof-$DevID\" cmd /c \"adb -s $DevID shell lsof > lsof.txt\"";
}
sub dumpsysMeminfo
{
system " start \"dumpsysMeminfo-$DevID\" cmd /c \"adb -s $DevID shell dumpsys meminfo > dumpsysMeminfo.txt\"";
}
sub procrank
{
system " start \"procrank-$DevID\" cmd /c \"adb -s $DevID shell procrank > procrank.txt\"";
}