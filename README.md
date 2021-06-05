# TextScramble
 [CLI] make text scrambled

안타깝게도 GUI 구현은 못하기 때문에 py 원본 자체로 올렸다.  
모든 파일의 인코딩은 utf-8로 되어있어야 정상 작동한다.

## TextBook.py
같은 경로 내에 py.txt를 만들어서 안에 영어 분문을 넣어준다. (줄 단위 구분)

Her dream is to become a comics artist.  
But after a few weeks, she starts skipping classes.  
Mr. Jo, the artist teacher, asks her to come to art class for a talk.  

이런 식으로 한 줄씩 적어주면 된다, 그 후 실행하면

to / dream / artist. / a / Her / comics / is / become  
few / starts / skipping / a / classes. / But / weeks, / she / after  
teacher, / her / come / art / for / a / Mr. / artist / Jo, / talk. / to / the / to / class / asks  

라는 내용과 함께 outputtext.txt라는 파일로 나온다.

## TwoFilesLines.py (UTf-8)
같은 경로 내에 first.txt (한글 뜻), second.txt (뒤섞인 영어 문장 파일)

그녀의 꿈은 만화가가 되는 것이어서, 그녀는 방과 후 활동 중 미술 프로그램에 참여한다.  
to / dream / artist. / a / Her / comics / is / become  

그러나 몇 주 후에, 그녀는 수업을 빠지기 시작한다.  
few / starts / skipping / a / classes. / But / weeks, / she / after  

이런 식으로 나온다. (앞에 문장 순서를 원하면 first 파일에 1. 2. ... 이렇게 추가해주면 된다)  
참고로 first, second 파일은 줄 수가 같아야 한다. 아님 오류가 발생한다. 아마?
