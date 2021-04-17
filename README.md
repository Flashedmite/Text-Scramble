# TextScramble
 [CLI] make text scrambled

아직 실력 부족으로 GUI 버전은 무리다, 나중에 한 번 만들어보도록 해야겠다..
나중에 교과서 모든 문장을 대상으로도 할 수 있게 할 거지만, 일단 지금 당장 필요한 정도만 만들었다.
실행하려면 Python3 설치가 되어있어야 한다.


# TextBook.py

같은 경로 내에 py.txt를 만든다. 안에 내용은
Her dream is to become a comics artist.
But after a few weeks, she starts skipping classes.
Mr. Jo, the artist teacher, asks her to come to art class for a talk.

이런 식으로 한 줄씩 적어주면 된다, 그 후 실행하면
to / dream / artist. / a / Her / comics / is / become
few / starts / skipping / a / classes. / But / weeks, / she / after
teacher, / her / come / art / for / a / Mr. / artist / Jo, / talk. / to / the / to / class / asks

라는 내용과 함께 outputtext.txt라는 파일로 나온다.


#TwoFilesLines.py (UTf-8):

first.txt (한글 뜻 추천), second.txt (영어 스크램블 파일 추천) 를 두고 실행하면

1. 그녀의 꿈은 만화가가 되는 것이어서, 그녀는 방과 후 활동 중 미술 프로그램에 참여한다.
to / dream / artist. / a / Her / comics / is / become


2. 그러나 몇 주 후에, 그녀는 수업을 빠지기 시작한다.
few / starts / skipping / a / classes. / But / weeks, / she / after

이런 식으로 나온다. (앞에 숫자는 내가 넣어준거임, 이것도 나중에 프로그램에 추가해야겠다.)
