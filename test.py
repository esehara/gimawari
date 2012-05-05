# -*- coding: UTF-8 -*-
import nose
from gimawari.console import parse_args
from nose.tools import *

def tt_pattern(arg_string):
	return parse_args(["gimawari",arg_string])

def parse_one_args_test():
	eq_(tt_pattern("しろ")  ,"git init")
	eq_(tt_pattern("みせて"),"git diff HEAD")
	eq_(tt_pattern("ぜんぶ"),"git add -u")
	eq_(tt_pattern("すべて"),"git add -u")
	eq_(tt_pattern("たいひ"),"git stash save")

def parse_first_alpha_test():
	eq_(tt_pattern("hoge　いれて"),"git add hoge")
	eq_(tt_pattern("hoge　いらない"),"git rm hoge")
	eq_(tt_pattern("hoge　はじめる"),"git checkout -b hoge")
	eq_(tt_pattern("hoge　つかう"),"git checkout hoge")
	eq_(tt_pattern("hoge　おわり"),"git checkout -d hoge")

def parse_first_commit_test():
	eq_(tt_pattern("コミット　とりけす"),"git reset HEAD^")
	eq_(tt_pattern("コミット　コメント　まちがえた"),"git commit --amend")
	eq_(tt_pattern("コミット　ほげほげ　です"),'git commit -m "ほげほげ"')

def parse_stash_test():
	eq_(tt_pattern("たいひ　かいしゅう"),"git stash pop")
	eq_(tt_pattern("たいひ　みせて"),"git stash list")
	eq_(tt_pattern("たいひ　はんえい"),"git stash apply")
	eq_(tt_pattern("たいひ　けす"),"git stash drop")

if __name__ == "__main__" : nose.main()
