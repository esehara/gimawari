def show_combinient_help():
	print ("""
    ぎまわり -- Gimawari

    設定系
    Vim   -> git config --global core.editor vim
    Emacs -> git config --global core.editor emacs
    いろつき -> git config --global color.ui auto

    ギッハブよろしく hoge/hoge -> git remote add origin git@github:hoge/hoge
    ギッハブよろしく hoge/hoge github -> git remote add github git@github:hoge/hoge
    グラフにして  -> git log --graph --date-order --all --date=short --oneline
    hogehoge.py 無視 -> .gitignore + hogehoge.py
	""")

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

    Log系::

    さいしん        -> git log -1 HEAD 

    Add & Commit系 ::

    ぜんぶ           -> git add -u
    hoge.py いれて   -> git add hoge.py
    hoge.py いらない -> git rm hoge.py
    hoge.py まぜない -> git rm --cached hoge.py
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

    べんり -> コマンド表示
    
	""")
