方法1：使用dmg安装
Download OS X emacs，拷贝到/Applications目录 
注意在终端运行emacs时很可能会运行OS X默认安装的emacs程序，/usr/bin/emacs，在~/.bash_profile中添加 
alias emacs=/Applications/Emacs.app/Contents/MacOS/Emacs 
然后 source ~/.bash_profile 
来定位emacs命令到自己安装的emacs上 emacs -nw 
