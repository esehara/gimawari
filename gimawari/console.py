#/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys,re
import gimawari_config
import subprocess

args = sys.argv

def show_commit_help():
	print ("""
    ぎまわり -- Gimawari

    「なにで困ってるんだい？」

    コミット コメント まちがえた -> git commit --amend
    コミット とりけす        -> git reset HEAD^ 
    コミット まきもどす      -> git reset --soft HEAD
    
    マージ とりけす -> git reset --hard ORIG_HEAD
    
    リベース とりけす -> git rebase --abort
    
    リセット しっぱい -> git reflog
    """)

def show_help():
	print("""
    ぎまわり -- Gimawari

    Gimawariは、Gitまわりを日本語で手助けするツールです。

    しろ                        -> git init
    とってきて/かいしゅう       -> git pull
    
    hoge/fuga へ おねがい/よろしく/たのむ/まかせた
        -> git status && git push hoge fuga

    Branch系::
    
    hoge はじめる    -> git checkout -b hoge
    hoge つかう      -> git checkout hoge
    hoge おわり      -> git checkout -d hoge

    Diff系::

    みせて           -> git diff HEAD

    Add & Commit系 ::

    ぜんぶ           -> git add -u
    hoge.py いれて   -> git add hoge.py
    hoge.py いらない -> git rm hoge.py
    コミット hogehoge です    -> git commit -m "hogehoge"
    hoge あわせて    -> git marge

    Stash系::
    たいひ           -> git stash save
    たいひ かいしゅう-> git stash pop
    たいひ みせて    -> git stash list
    たいひ はんえい  -> git stash apply
    たいひ けす      -> git stash drop

    !! 困ったーーーーー !!

    たすけて -> コマンド表示

    !! べんり !!
    
    ギッハブよろしく hoge/hoge -> git remote add origin git@github:hoge/hoge
    ギッハブよろしく hoge/hoge github -> git remote add github git@github:hoge/hoge
	グラフにして  -> git log --graph --date-order --all --date=short --oneline
	hogehoge.py 無視 -> .gitignore + hogehoge.py
	""")
def add_ignorefile(targetfile):
	print ".gitignore に " + targetfile + " を追加しました。"
	ignorefile = open(".gitignore","a")
	ignorefile.write(targetfile + "\n")
	ignorefile.close()
	exit()

def parse_args(args):
	temp_args = []
	zenkuhaku = re.compile("　")
	for arg in args: temp_args = temp_args + arg.decode("UTF-8").split(u"　")
	args = []
	for i,item in enumerate(temp_args): args.append(item.encode("UTF-8"))
	if len(args) == 2:
		for conf in gimawari_config.argone_list():
			if args[1] == conf[0]:return conf[1]
	if len(args) == 3:
		if args[1] == "ぜんぶ" and args[2] == "いれて": return "git add -a"
		if args[1] == "たいひ":
			if args[2] == "かいしゅう": return "git stash pop"
			if args[2] == "みせて"  : return "git stash list"
			if args[2] == "はんえい": return "git stash apply"
			if args[2] == "けす"    : return "git stash drop"
		alphabet = re.compile("^(\w|.)+$")
		if alphabet.search(args[1]):
			if args[2] == "無視"    : add_ignorefile(args[1])
			for conf in gimawari_config.first_alpha():
				if args[2] == conf[0]:return conf[1] + " " + args[1]
	if args[1] == "コミット":
		if len(args) == 3:
			if args[2] == "とりけす": return "git reset HEAD^"
			if args[2] == "まきもどす": return "git reset --soft HEAD^"
		if len(args) > 3:
			if args[3] == "です": return 'git commit -m "' + args[2] + '"'
			if args[2] == "コメント" and args[3] == "まちがえた": return "git commit --amend"

	if args[1] == "マージ":
		if args[2] == "とりけす": return "git reset --head ORIG_HEAD"

	if args[1] == "リベース":
		if args[2] == "とりけす": return "git rebase --abort"

	if args[1] == "リセット":
		if args[2] == "しっぱい": return "git reflog"

	if args[1] == "ギッハブよろしく":
		if len(args) == 3:return "git remote add origin git@github:" + args[2]
		if len(args) == 4:return "git remote add " + args[3] + " git@github:" + args[2]

	if len(args) == 4:
		if args[2] == "へ" and (args[3] == "おねがい" 
				or args[3] == "よろしく" 
				or args[3] == "たのむ"
				or args[3] == "まかせた"):git_push(args[1])
	
	if args[1] == "たすけて":
		show_commit_help()
		exit()
	
	print "ごめん、それわからない"
	exit()

def git_push(origin_master):
	print subprocess.check_output("git status",shell=True)
	yes_or_no = raw_input("「これでいいんだね？」(はい / いいえ)")
	if yes_or_no == "はい":
		origin_master = origin_master.split("/") 
		print subprocess.check_output("git push " + origin_master[0] + " " + origin_master[1],shell=True)
		exit()
	else:
		print "「じゃあね」"
		exit()

def begin():
	if len(args) == 1:
		show_help()
		sys.exit()
	run_string = parse_args(args)
	print "実行するわ => " + run_string
	print subprocess.check_output(run_string,shell=True)
	exit()

if __name__ == '__main__': begin()
