from utils.dotdict import dotdict

cfg = dotdict(
    TISTORY=dotdict(
        ID='leesoyun950628@gmail.com',
        PW='46566656wns!',
        BLOG_NAME='yunlee10',
        SECRET_KEY='7341d2efda36edc58aa80b1f65e438b889c33b32d9416e3048dab30adffd72c17efda9a5',
        CLIENT_ID='7341d2efda36edc58aa80b1f65e438b8',
        REDIRECT_URI='https://yunlee10.tistory.com/',
    ),

    NOTION=dotdict(
        TOKEN_V2='v02%3Auser_token_or_cookies%3Am_HIwCMwOd5iDhC68Z6oAN2rBqVaf2jQ1axCNwbLtjVUrmfaehxs0nw6C4tOhu662kgdM_EGuekqVf0lphGVkQ4wEJ49jbUT-qq2YUbBp-JrN_lVCdw6477XpWCDf0qxl34m',
        TABLE_PAGE_URL='https://www.notion.so/384b550c5bad498089e3b0ccb59d41ad?v=7774e67e13fb4613ad02cca322ff9e11&pvs=4',
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
