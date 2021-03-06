https://doc.pfsense.org/index.php/Remount_embedded_filesystem_as_read-write
To remount file systems as read-write, run:

/etc/rc.conf_mount_rw

To mount as read-only again, run:

/etc/rc.conf_mount_ro

On pfSense 2.1, you can make this change in the GUI under Diagnostics > NanoBSD, using the toggle button there. 


 $ pwd
 /test/pfsense_www
# vi fend.inc 
 All Right Reserved


# Disable boot menu&logo
#Edit /boot/loader.conf
autoboot_delay="3"
beastie_disable="YES"


# Logo about
 cat /etc/ascii-art/pfsense-logo-small.txt
/etc/rc.banner

1. 首先设置字符集，pfsense 的默认字符集是 iso-8859-1，必须将其改为 utf-8, 这样才能将汉字正确的显示出来，否则显示出来的是乱码。主要修改以下三个文件:
/usr/local/www/head.inc
/usr/local/www/index.php
/usr/local/www/graph.php
将 iso-8859-1 改为 utf-8

2.  修改菜单文件
菜单文件为:
/usr/local/www/fbegin.inc
将各对应菜单项修改成相应中文即可。

3. 修改页面内容
修改 /usr/local/www/ 下各 php文件，将各对应英文改成中文即可。

4, Silence boot
You could try boot_mute.

