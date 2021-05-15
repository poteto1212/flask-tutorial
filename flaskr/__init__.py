#アプリケーションファクトリーを含むファイル
#flaskerディレクトリをパッケージとして使えるようにする

import os#osモジュール
from flask import Flask

#アプリ機能に関する関数
#test_config引数の標準はnone→引数無しでもありでも呼び出し可能
def create_app(test_config=None):
    #モジュール名及び相対パスからのファイル参照を可能にする
    app=Flask(__name__,instance_relative_config=True)
    
    #アプリの標準設定
    app.config.from_mapping(
        SECRET_KEY="dev",#セキュリティ対策。本番環境時は鍵として機能するのでランダムな値を設定
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')#現階層にDBファイルを自動生成
        )
        
    #引数ない時
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)#インスタンスフォルダにconfig.pyがある時はそれを使う
    #引数ある時
    else:
        app.config.from_mapping(test_config)#引数のファイルを設定に追加
        
    
    #例外発生の有無による処理の条件分岐
    try:#例外発生時も実行
        os.makedirs(app.instance_path)#設定ファイル群(インスタンスフォルダ)へのパスを保持
    except OSError:#例外発生時に行う
        pass
    
    
    #アプリルーティング
    @app.route('/hello')
    def hello():
        return 'Hello,World!'
        
    return app
    