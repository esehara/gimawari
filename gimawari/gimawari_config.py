# -*- coding:UTF-8 -*-
def argone_list():
	return ([
				["しろ","git init"],
				["みせて","git diff HEAD"],
				["とってきて","git pull"],
				["かいしゅう","git pull"],
				["ぜんぶ","git add -u"],
				["すべて","git add -u"],
				["グラフにして","git log --graph --date-order --all --date=short --oneline"],
				["たいひ","git stash save"],
				["さいしん","git log -1 HEAD"],
				["いろつき","git config --global color.ui true"],
				["いろなし","git config --global color.ui false"],
				["Vim","git config --global core.editor vim"],
				["emacs","git config --global core.editor emacs"],
			])

def first_alpha():
	return ([
				["いれて","git add"],
				["いらない","git rm"],
				["まぜない","git rm --cached"],
				["あわせて","git marge"],
				["はじめる","git checkout -b"],
				["つかう","git checkout"],
				["おわり","git checkout -d"],
			])
