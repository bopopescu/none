::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ��BAT�ű���ҪĿ����Ϊ��ʵ�ֶ�ʱ���Ų��Զ�����ָ������վ���ض���ʱ�䷶Χ�������µ���ҳ��
:: Created By Merlyn
:: # License:      GPL
:: # License file  LICENSE.txt
:: # Email:        merlyncaulfield@gmail.com
:: #
:: # -----------------------------------------------------------------------------
:: # This program is free software; you can redistribute it and/or
:: # modify it under the terms of the GNU General Public License
:: # as published by the Free Software Foundation; either version
:: # 2 of the License, or (at your option) any later version.
::
::
:: # This program is distributed in the hope that it will be useful, but WITHOUT
:: # ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
:: # FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
:: # more details.
::
:: # You should have received a copy of the GNU General Public License along with
:: # this program; if not, write to the Free Software Foundation Inc., 59 Temple
:: # Place - Suite 330, Boston, MA 02111-1307, USA.
:: # -----------------------------------------------------------------------------
::
:: Last updated 04/18/2013
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@echo off
set /P today="������ʱ��(��ʽΪ 201304/04 �� 201304/03|201304/04 ): " || echo ���ڲ���Ϊ��!!! && pause && exit 
set /p time1="�����벦�����Ӽ��ʱ��: " 
set SITE=www.zjpy.gov.cn

::ִ��Hide_BAT_CMD.vbs
set BROWSER=Hide_BAT_CMD.vbs
@RMDIR /S /Q %SITE% 2>nul

:begin
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ���жϡ��������ӡ����������ӡ�
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::�������Ӽ��ʱ��
ping -n %time1% 127.0.0.1 >nul
RASDIAL PPPOE /disconnect && echo ���������ѶϿ�! || echo �Ͽ�ʧ��
ping -n 2 127.0.0.1 >nul
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: �޸ĳɴ���ʱ����д��PPPOE��������
:: username password�滻Ϊ�Լ���PPP�����û��������롣
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
RASDIAL PPPOE username password

echo LET'S GO!  
echo "ͬ��������ҳ���ѽ���ض���urls.txt�����Ե�..."

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ģ������ض�ʱ�䷶Χ�������µ���ҳ����
:: ��ʵ�ַ�ʽΪ��wget�����Ȱ�ָ������վҳ�����ػ�������֮��ÿ��ֻ���ظ��µĲ�����ҳ��
:: Ȼ���ҳ�ĳ��ʱ���ڸ��µ���ҳ����sed����ת����url������urls.txt�У����������chrome,firefox��
:: ���ʸ�urls.txt�е���ҳ���ӣ��Ӷ��ﵽ�˷��ʺ�ˢ�µ�Ŀ�ġ�
:: ���ͬʱ�ű���ѷ��ʵĽ���ض���autodial_log.txt�ļ��У���������ʱ���¼���Լ���IP��ַ�����ʳɹ���ʧ�ܵĽ����
:: @DIR /B /W /S %SITE% | findstr "201304.04.*html"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 

@TASKLIST | @FINDSTR "chrome.exe" 1>nul 2>nul & start %BROWSER% & wget -o wget.log --accept="html" --user-agent="Mozilla/5.0 (IPad; u; CPU OS 3_2_1 like Mac OS X; en-us) applewebkit/531.21.10 (khtml, like gecko) mobile/7b405" --continue --recursive --no-parent --no-clobber http://%SITE%/ 2>nul & @DIR /B /W /S %SITE% | gfind %SITE% -type f -name "*.html" | sed -e "s/www/http:\/\/www/;s/\\/\//g" | grep -E "%today%" > urls.txt & @TYPE urls.txt | gawk -F"20" "{ print $1 }"  | sed "s/.$/index.html/" | uniq -i >> urls.txt & unix2dos urls.txt 1>nul & echo http://%SITE% >> urls.txt &  echo ָ������������������ҳ�������ҵ�������urls.txt�ļ���! & echo ��������... & multiurls.bat urls.txt 1>nul & ping -n 3 127.0.0.1 >nul && multiurls.bat urls.txt 1>nul & ping -n 2 127.0.0.1 >nul & @TASKKILL /F /IM "chrome.exe" 1>nul & wget -q -O - icanhazip.com 1>> autodial_log.txt 2>nul && echo %DATE% %TIME% Successful. >> autodial_log.txt || echo %DATE% %TIME% Failed! >> autodial_log.txt

goto begin
pause >nul
