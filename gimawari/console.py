#/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys,re
import gimawari_config
import subprocess

args = sys.argv

def show_commit_help():
	print ("""
    ぎまわり -- Gimawari

    「コミットのなにで困ってるんだい？」

    コミット コメント まちがえた -> git commit --amend
    コミット とりけす        -> git reset HEAD^ 
    """)

def show_help():
	print("""
    ぎまわり -- Gimawari

    Gimawariは、Gitまわりを日本語で手助けするツールです。

    しろ             -> git init
    とってきて       -> git pull
    おねがい         -> git status && git push

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

    !! 困ったーーーーー !!

    コミット たすけて -> コマンド表示

    !! べんり !!
    
    ギッハブよろしく hoge/hoge -> git remote add origin git@github:hoge/hoge
	ギッハブよろしく hoge/hoge github -> git remote add github git@github:hoge/hoge
    """)

def parse_args(args):
	zenkuhaku = re.compile("　")
	if zenkuhaku.search(args[1]):
		temp_args = args[1].decode("UTF-8").split(u"　")
		args = ["gimawari"]
		for i,item in enumerate(temp_args): args.append(item.encode("UTF-8"))
	if len(args) == 2:
		for conf in gimawari_config.argone_list():
			if args[1] == conf[0]:return conf[1]
		if args[1] == "おねがい":git_push()
	if len(args) == 3:
		if args[1] == "ぜんぶ" and args[2] == "いれて": return "git add -a"
		alphabet = re.compile("^(\w|.)+$")
		if alphabet.search(args[1]):
			for conf in gimawari_config.first_alpha():
				if args[2] == conf[0]:return conf[1] + " " + args[1]
	if args[1] == "コミット":
		if len(args) == 3:
			if args[2] == "たすけて":
				show_commit_help()
				exit()
			if args[2] == "とりけす": return "git reset HEAD^"
		if len(args) > 3:
			if args[3] == "です": return 'git commit -m "' + args[2] + '"'
			if args[2] == "コメント" and args[3] == "まちがえた": return "git commit --amend"

	if args[1] == "ギッハブよろしく":
		if len(args) == 3:return "git remote add origin git@github:" + args[2]
		if len(args) == 4:return "git remote add " + args[3] + " git@github:" + args[2]

	print "ごめん、それわからない"
	exit()

def git_push():
	subprocess.check_output("git status",shell=True)
	yes_or_no = raw_input("「これでいいんだね？」(はい / いいえ)")
	if yes_or_no == "はい":
		subprocess.check_output("git push",shell=True)
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
