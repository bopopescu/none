VRM     ֱ����-ֱ������ѹ�����ֹ��ϻ�ʧ��CNFG�������ô���
NMI  Ӳ�������ѱ��������ϵͳ��ע��PCI ��MEM ָʾ��Ҳ���ܻ������
SP         Remote Supervisor Adapter II �������ϻ�ȱ�٣�����δ���ӱ�ƽ���¡�
DASD    Ӳ���������������ϻ���ж��
RAID    RAID ������ָ�������˹���
FAN   ���ȷ������ϻ���ж��
BRD  ΢���������I/O �巢������

CNFG  �������ô���
NMI      Ӳ�������ѱ��������ϵͳ��

VRM   һ����CPU��Դģ����ϡ�CPU�����Ҳ������
NMI   һ�����ڴ����ָ�������δ����ڴ渽�����е�����Ҳ������PCI���ϡ����������PCI�����ϣ�PCI�۸����ƻ�����
DASD  һ����Ӳ�����⡣Ӳ���ϱ���ƻ������������Ļ������п�����ʾ��
FAN   ��Ȼ�Ƿ��ȹ����ˡ���Ӧ�ķ��ȵƻ�����
PS1/PS2 һ·��Դ�����⡣ͨ����ֻ����һ·�硣��������ˣ���������£���Դ����AC��DCӦ�ö����������Դ����

90%���������Ϲ��ϡ�
������ָʾ�ƾ����������������н���~


���ش𼸸��ɣ������Ǻ�ȫ�棬 ֪���Ķ�˵������˵������Ҫ�ļ�����
ps1 ��Դ1
ps2 �����Դ2
cpu cpu
vrm cpu��ѹģ��
mem �ڴ�
raid raid���п�
fan ����������
brd pci ����pci����ϵ��豸

�Ǹ�����ƣ��ͱ�ʾ�ĸ��豸�й���

DS3500 reset password
http://www.filibeto.org/unix/aix/lib/hardware/ds4800/faq/QOW-LD%20Forgotten%20Password.htm
http://www.bvanleeuwen.nl/faq/?p=8
http://tecniq.info/index.php/DS_Subsystem_CLI_access_and_commands

For the serial connection, choose the correct port and the following settings:

    57600 Baud
    8 Data Bits
    1 Stop Bit
    No Parity
    Xon/Xoff Flow Control 

Send a break signal to the controller. This varies depending on the terminal emulation. For most terminal emulations, such as HyperTerm, which is included in Microsoft Windows products, press Ctrl+Break. If you only receive unreadable characters, press Ctrl+Break again, until the following message appears:

Press <SPACE> for baud rate within 5 seconds.

Press the Space bar to ensure the correct baud rate setting. If the baud rate was set, a confirmation appears. Press Ctrl+Break to log on to the controller. The following message appears:

Press within 5 seconds: <ESC> for SHELL, <BREAK> for baud rate.

Press the Esc key to access the controller shell. The password you are prompted for is infiniti. Note that this appears to have changed for the DS4700 and DS4800 systems and the serial connections are not longer directly supported.
Password Reset

To reset the storage manager password you need to log into each DS controller via the serial CLI and use the following command (case sensitive):  

    clearSYMbolPassword 
