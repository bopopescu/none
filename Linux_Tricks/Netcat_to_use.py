		Niubility Tool Netcat.
## netcat ɨ��˿�
nc -v -w 2 localhost -z 1-65535

## chat server
server: nc -l -p 11111 
client: nc 10.7.84.111 11111

## Suppose you want to send files in /data from computer A with IP 192.168.2.111 to computer B(with any IP), It's as simple as this:
server: $ tar -cf - /data | pv | nc -l -p 6666 -q 3
client: $ nc 192.168.2.111 6666 | pv | tar -xf -
OR:	$ tar -cf - /data | pv | gzip | nc -l -p 6666 -q 3
	$ nc 192.168.2.111 6666 | gunzip | pv | tar -xf -

## A single file can be sent even easier.
server: $ cat file | nc -l -p 6666 
OR( will more efficient ):
server: $ nc -l -p 6666 < file

client: $ nc 192.168.2.111 6666 > file

## And you may copy and restore whole disk with nc:
server: $ cat /dev/sda | nc -l -p 6666
cliend: $ nc 192.168.2.111 6666 > /dev/sda

## As a proxy
$ nc -l -p 12345 | nc www.google.com 80
$ nc -l -p 12345 | nc www.google.com 80 | nc -l -p 12346

## Probably the most powerful netcat's feature is making any process a server:
$ nc -l -p 12345 -e /bin/bash
client: $ nc 10.7.84.111 12345 (then you may use bash:)

## $Backup whole server!
## --same-owner 
##
tar cvzp --exclude=/root/backup.log --exclude=/proc/* --exclude=/media/* --exclude=/dev/* --exclude=/mnt/* --exclude=/sys/* --exclude=/tmp/* / 2>/root/backup.log | nc -w 3 REMOTE_IP -l -p 6666 -q 5
tar -cp --exclude=/root/backup.log --exclude=/proc/* --exclude=/dev/* --exclude=/sys/* --exclude=/tmp/* / 2>/root/backup.log |  pv | nc -vv -n -w 60 -l -p 6666 -q 3

nc 218.75.24.181 6666 >/root/backup.tgz

#Restore Your Backup

tar -xvpzf /home/backup.tgz -C / 

##Restoring Over a Network

This short guide, assumes you employed nc to make the original backup as described above.
#######################################################
## Tar backup and restore
#######################################################
#Receiving Computer
Ensure the disk has been mounted and use the following command to accept input over the network that will then be extracted to the path indicated. In this example, the directory /mnt/disk will be extracted to.

nc 10.7.84.26 6666 | tar -xvp(z/j)f - -C /mnt/disk 

#Sending Computer
On the computer with the archive to send, use the following command:

cat backup.tar.gz | nc -l 6666 
#######################################################



#$this is basically copying a compressed partition or disk over the network, unencrypted. you may consider using ssh for safety reasons, e.g:

foo:# cat /dev/sda | bzip | ssh remotehost "cat > /backup/foo.sda.bz2"

I don��t see any good about using ssh in local network and it would produce extra traffic. Here��s my contrib to backup and restore a linux parition:

# BACKUP �C to backupserver (192.168.1.1)
nc -p 2222 -l | bzip2 -c > Image.bz2
# BACKUP �C from clienthost (192.168.1.2)
dd if=/dev/sda bs=16M | nc 192.168.1.1 2222
>>> dd if=/dev/sda bs=16M | nc -vv -n -l -p 3333 -w 60 -q 5

# RESTORE �C to clienthost (192.168.1.2)
nc -p 2222 -l > /dev/sda
>>> time nc -vv 192.168.1.111 3333 | dd of=/dev/sda
# RESTORE �C from backupserver (192.168.1.1)
dd if=Image.bz2 bs=16M | bunzip2 -c | nc 192.168.1.2 2222

# Transferred server directory to client machine with progress bar.
server: tar -cf - /mnt/sda6/books/Linux_newbie/ | pv -s $(du -sb . | awk '{print $1}') | nc -l -p 6666 -q 3
OR:     tar -cf - /mnt/sda6/books/Linux_newbie/ | pv -s $(du -sb . | cut -f1) | nc -l -p 6666 -q 3
client: nc server_ip 6666 | pv | tar -xf -


## Play music !!!
server: cat windflowers.mp3 | pv | nc -l -p 6666 -q 3
client: nc REMOTE_IP 6666 | mpg123 -v -C -
OR:
server: cat windflowers.mp3 | pv -s $(du -sb . | awk '{ print $1 }') | nc -l -p 6666 -q 3
%server: for i in `find . -name "*.mp3"` do cat $i | pv -s $(du -sb . | awk '{ print $1 }') | nc -l -p 6666 -q 3
client: nc REMOTE_IP 6666 | mpg123 -v -C -

tar cvzp --exclude=backup.log ./ 2>backup.log | pv -s 1753167806 | nc -l -p 6666 -q 5 

dd bs=1M if=/dev/sda | gzip | ssh user@ip_addr 'dd of=sda.gz' 

( tar -c /dir/to/copy ) | ssh -C user@remote 'cd /where/to/ && tar -x -p'   Copy (with permissions) copy/ dir to remote:/where/to/ dir

dd bs=1M if=/dev/sda | gzip | ssh user@remote 'dd of=sda.gz' Backup harddisk to remote machine


[root@cal-7-3 ~]# sudo sfdisk -luS /dev/sda
   Device  Boot  Start      End  #sectors  Id  System
  /dev/sda1     *   2048  2050047   2048000  83  Linux
 
  #  dd up to the last sector, rounded up for simplicity.

  dd if=/dev/sda bs=512 count=2100000 conv=notrunc | gzip | ssh 192.168.1.254 'gzip -d | dd of=/root/my-image'

  http://superuser.com/questions/716089/dd-a-partition-and-keep-device-structure
http://ubuntuforums.org/showthread.php?t=1840320#post_11234165
