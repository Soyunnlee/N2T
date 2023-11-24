from utils.dotdict import dotdict

cfg = dotdict(
    TISTORY=dotdict(
        ID='leesoyun950628@gmail.com',
        PW='46566656wns!',
        BLOG_NAME='soyun-s',
        SECRET_KEY='89b2a505f1efbc1753297b6e42aca830aa62ba62af373ce5302b8798ab58989c5382834b',
        CLIENT_ID='89b2a505f1efbc1753297b6e42aca830',
        REDIRECT_URI='https://soyun-s.tistory.com',
    ),

    NOTION=dotdict(
        TOKEN_V2='v02%3Auser_token_or_cookies%3Am_HIwCMwOd5iDhC68Z6oAN2rBqVaf2jQ1axCNwbLtjVUrmfaehxs0nw6C4tOhu662kgdM_EGuekqVf0lphGVkQ4wEJ49jbUT-qq2YUbBp-JrN_lVCdw6477XpWCDf0qxl34m',
        TABLE_PAGE_URL='https://www.notion.so/92be706088ba4fe4a29ed6145c462de8?v=a7089673fa69427f88eff69b15c3af4a&pvs=4',
        DOWNLOAD_DIR='~/.n2t',
        CODE_BLOCK_THEME='atom-one-dark',

        COLUMN=dotdict(
            TITLE='제목',
            CATEGORY='카테고리',
            TAG='태그',
            STATUS='상태',
            URL='링크'
        ),

        POST=dotdict(
            UPLOAD_VALUE='발행 요청',
            MODIFY_VALUE='수정 요청',
            COMPLETE_VALUE='발행 완료',
        ),
    ),

    MAIL=dotdict(
        ID='',
        KEY='',
    )
)
