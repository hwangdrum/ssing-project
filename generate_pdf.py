from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# 폰트 등록
pdfmetrics.registerFont(TTFont('NanumGothic', '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'))
pdfmetrics.registerFont(TTFont('NanumGothicBold', '/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf'))

W, H = A4
doc = SimpleDocTemplate(
    '/home/user/ssing-project/사전과제_작성본.pdf',
    pagesize=A4,
    rightMargin=20*mm,
    leftMargin=20*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
)

# 스타일 정의
def style(name, font='NanumGothic', size=10, leading=18, color=colors.black, bold=False, space_before=0, space_after=6, left_indent=0):
    return ParagraphStyle(
        name,
        fontName='NanumGothicBold' if bold else 'NanumGothic',
        fontSize=size,
        leading=leading,
        textColor=color,
        spaceAfter=space_after,
        spaceBefore=space_before,
        leftIndent=left_indent,
    )

s_title     = style('title',    size=20, leading=26, bold=True, space_before=0, space_after=10)
s_part      = style('part',     size=14, leading=20, bold=True, color=colors.HexColor('#1a1a2e'), space_before=14, space_after=6)
s_tag       = style('tag',      size=9,  leading=14, color=colors.white, bold=True)
s_label     = style('label',    size=10, leading=16, bold=True, color=colors.HexColor('#555555'), space_before=10, space_after=4)
s_body      = style('body',     size=10, leading=18, space_before=2, space_after=4)
s_example   = style('example',  size=10, leading=18, color=colors.HexColor('#444444'), space_before=2, space_after=4, left_indent=4)
s_mine      = style('mine',     size=10, leading=18, color=colors.HexColor('#1a3a6b'), space_before=2, space_after=4, left_indent=4)
s_table_h   = style('table_h',  size=9,  leading=14, bold=True, color=colors.white)
s_table_b   = style('table_b',  size=9,  leading=14)
s_keyword   = style('keyword',  size=12, leading=18, bold=True, color=colors.HexColor('#1a3a6b'), space_before=4, space_after=4, left_indent=8)
s_note      = style('note',     size=8,  leading=13, color=colors.HexColor('#888888'), space_before=2, space_after=2)
s_caption   = style('caption',  size=9,  leading=14, color=colors.HexColor('#666666'), space_before=2, space_after=8, bold=True)

def section_box(label, bg_color='#1a1a2e'):
    data = [[Paragraph(label, s_tag)]]
    t = Table(data, colWidths=[W - 40*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_color)),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def divider(color='#cccccc'):
    return HRFlowable(width='100%', thickness=0.5, color=colors.HexColor(color), spaceAfter=6, spaceBefore=6)

story = []

# ── 표지 ──────────────────────────────────────────────
story.append(Spacer(1, 30*mm))
story.append(Paragraph('씽프로젝트 (Cing Project)', style('cover_sub', size=12, color=colors.HexColor('#888888'), space_after=4)))
story.append(Paragraph('아이덴티티 디자인 사전과제', style('cover_title', size=22, leading=30, bold=True, space_after=6)))
story.append(Paragraph('작성자 본인 제출본', style('cover_desc', size=10, color=colors.HexColor('#aaaaaa'), space_after=40)))
story.append(divider('#dddddd'))
story.append(Spacer(1, 8*mm))
story.append(Paragraph('이 문서는 원본 PDF의 각 파트 안내 및 예시 다음에 작성자의 실제 답변이 배치된 형식입니다.', s_note))
story.append(Spacer(1, 60*mm))

# ── PART 1 ────────────────────────────────────────────
story.append(section_box('PART 1.  Lifeline Discovery'))
story.append(Spacer(1, 4*mm))
story.append(Paragraph('안내', s_label))
story.append(Paragraph(
    '아이덴티티를 찾는 작업은 바로, 여기에서부터 시작합니다. 나에게 일어난 수많은 사건들 중에서 내가 다른 사건보다 좀 더 중요하게 '
    "'의미'를 부여하는 사건이 무엇인지 떠올려보면서, 인생곡선을 그려보세요. 사건은 10개 내외로 정리해보면 좋습니다.", s_body))
story.append(Spacer(1, 2*mm))

story.append(divider())
story.append(Paragraph('✦ 내 작성 — Lifeline', s_caption))

# Lifeline 표
table_data = [
    [Paragraph('나이', s_table_h), Paragraph('사건', s_table_h), Paragraph('감정 / 통찰', s_table_h)],
    [Paragraph('4살', s_table_b), Paragraph('차에 치였지만 어른들은 과자만 주고 떠났다.', s_table_b), Paragraph('세상에 대한 첫 번째 의심. 사람은 검증이 필요한 존재다.', s_table_b)],
    [Paragraph('8살', s_table_b), Paragraph('좋아하는 친구에게 포옹을 했지만 상대는 기뻐보이지 않았다.', s_table_b), Paragraph('내 감정이 상대에게 그대로 닿지 않는다는 걸 처음 느낌. 사람을 관찰해야 한다.', s_table_b)],
    [Paragraph('13살', s_table_b), Paragraph('전교 회장 선거에 나가 부회장이 됐다.', s_table_b), Paragraph('아쉬움이 동력이 된다는 것을 배움.', s_table_b)],
    [Paragraph('15살', s_table_b), Paragraph('밤새 공부해 전교 36등을 달성했다.', s_table_b), Paragraph('하는 만큼 나온다. 노력과 결과 사이의 직선을 처음 발견함.', s_table_b)],
    [Paragraph('16살', s_table_b), Paragraph('농구에 빠져 학교 끝나고 밤늦게까지 코트에 있었다.', s_table_b), Paragraph('순수한 즐거움, 팀으로 움직이는 감각. 몰입이 뭔지 알게 됨.', s_table_b)],
    [Paragraph('18살', s_table_b), Paragraph('존경하는 코치 선생님이 교통사고로 갑자기 세상을 떠났다.', s_table_b), Paragraph('슬픔보다 먼저 온 멍함. 감정을 처리하는 방식에 대한 의문이 생김.', s_table_b)],
    [Paragraph('19살', s_table_b), Paragraph('연골 연화증 진단. 더 이상 격한 운동을 할 수 없게 됐다.', s_table_b), Paragraph('내가 원해도 안 될 수 있다. 의지와 현실 사이의 첫 충돌.', s_table_b)],
    [Paragraph('21살', s_table_b), Paragraph('디지털 산업디자인과 입학. 미술 출신들 사이에서 컴퓨터 디자인으로 두각.', s_table_b), Paragraph('나는 내 방식으로 잘하면 된다.', s_table_b)],
    [Paragraph('22살', s_table_b), Paragraph('군 복무 20개월. 교회에서 평생 친구를 얻었다.', s_table_b), Paragraph('소속되지 않아도 연결될 수 있다.', s_table_b)],
    [Paragraph('24살', s_table_b), Paragraph('유기견 봉사 동아리에서 다양한 대학생들과 교류.', s_table_b), Paragraph('생각 깊은 사람이 재미있다. 인생을 유익하게 써야겠다는 방향감각이 생김.', s_table_b)],
    [Paragraph('25살', s_table_b), Paragraph('"왜 뻔한 것만 만들어야 하냐"고 교수에게 질문했다가 학교생활이 힘들어졌다.', s_table_b), Paragraph('권위가 항상 옳지 않다. 맥락을 읽어야 한다는 것도 배움.', s_table_b)],
    [Paragraph('26살', s_table_b), Paragraph('아빠 회사에서 일했지만 관계가 어긋났다. 홍익대 국제대학원 합격.', s_table_b), Paragraph('스스로 선택한 환경에서 성장할 수 있음을 확인.', s_table_b)],
    [Paragraph('27살', s_table_b), Paragraph('대학원에서 믿었던 동기에게 배신을 당했다.', s_table_b), Paragraph('스스로 해결하는 힘이 길러짐.', s_table_b)],
    [Paragraph('28살', s_table_b), Paragraph('UC 샌디에고로 어학연수. 넓은 세상에서 다양한 국적의 친구들과.', s_table_b), Paragraph('인생에서 가장 행복했던 시간. 낯선 것이 위험이 아니라 가능성이라는 것을 느낌.', s_table_b)],
    [Paragraph('29~30살', s_table_b), Paragraph('핀란드 박사 진학을 위해 아이엘츠 6번 도전. 유럽 교수들에게 답장이 없었다.', s_table_b), Paragraph('통역과 프리랜서로 자립 가능성을 확인. 정규직이 답이 아닐 수 있다는 감각.', s_table_b)],
    [Paragraph('31~32살', s_table_b), Paragraph('AI를 만났다. 디자인 약점을 AI가 보완해줄 수 있다는 것을 발견.', s_table_b), Paragraph('나의 부족함이 약점이 아닐 수 있다. 도구를 통해 가능성이 열리는 경험.', s_table_b)],
    [Paragraph('33살', s_table_b), Paragraph('첫 정규직. 1년간 왕따를 당했다. 그럼에도 1년을 버티고 스스로 나왔다.', s_table_b), Paragraph('버텼다는 것 자체가 증명이 됨. 내가 잘되면 된다.', s_table_b)],
    [Paragraph('34살', s_table_b), Paragraph('부업과 프리랜서로 경제적 독립을 준비 중. 창업과 사업을 꿈꾸는 중.', s_table_b), Paragraph('아직 완성되지 않았다. 그게 지금의 나.', s_table_b)],
]
col_w = [(W-40*mm)*0.1, (W-40*mm)*0.42, (W-40*mm)*0.48]
t = Table(table_data, colWidths=col_w, repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f5f7ff'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.HexColor('#cccccc')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 6*mm))

# Lifeline 패턴
story.append(Paragraph('반복되는 패턴: 의심 → 관찰 → 도전 → 좌절 → 재발견', style('pattern', size=10, bold=True, color=colors.HexColor('#1a3a6b'), space_before=4, space_after=4)))
story.append(Spacer(1, 10*mm))

# ── PART 2 ────────────────────────────────────────────
story.append(section_box('PART 2.  My Story'))
story.append(Spacer(1, 4*mm))

story.append(Paragraph('안내', s_label))
story.append(Paragraph(
    '다음에 마련된 스토리 보드의 빈칸을 채워가며 당신의 이야기를 들려주세요. 빈칸을 채울 때에는 추상적인 단어나 단답형보다는 '
    '구체적인 느낌이나 행동을 표현하는 형용사나 동사를 사용해 적어보길 바랍니다.', s_body))

story.append(Spacer(1, 3*mm))
story.append(Paragraph('예시', s_label))
story.append(Paragraph(
    '성인이 되기 전, 내가 가장 행복했던 한 장면을 떠올려보라고 하면 <b>초등학교 때 학교 방송국에서 기자로 활동하던</b> 순간이 가장 먼저 떠오른다. '
    '그 이유를 곰곰이 생각해보면 그것이 나에게 <b>내가 알고 깨달은 무언가를 누군가에게 전달하는</b> 즐거움을 줬기 때문이다. '
    '성인이 된 후, 나에게 가장 큰 성취감을 안겨줬던 것은 <b>어떤 기업의 컨셉을 발견해주는 프로젝트</b>를 한 것이다. '
    '이때, 그 결과물을 떠나 <b>무언가를 아주 깊게 연구했을 때 창조적인 영감을 얻는 것</b>이 나는 굉장한 기쁨을 느끼는 사람이라는 것을 알게 되었다. '
    '무엇보다 지금까지의 삶에서 내 가슴을 가장 뜨겁게 했던 순간을 꼽으라고 한다면 아마도 <b>단 3명 앞에서 강의를 했을 때</b>다. '
    '왜냐하면 그때, <b>단 한 명이라도 누군가의 삶을 변화시키는 일을 하는 것이 얼마나 가치있는 일인지</b>를 느끼고, 깨달았기 때문이다. '
    '이러한 경험들이 쌓이면서 아마도 내가 처음으로 꾸었던 꿈은 <b>누군가의 삶을 변화시키고 성장시키는 즐거운 교육을 하는 것</b>이다. '
    '하지만 힘들었던 어떤 사건으로 인해 나는 오히려 <b>사람들을 변화시키려면 먼저 그들을 진정으로 사랑해야 함</b>을 깨달으며, 내 삶에서 이것이 얼마나 중요한 지를 알게 되었다. '
    '인생의 좌우명이랄까, 그것은 <b>"본질에는 일치를, 비본질엔 자유를, 모든 것엔 사랑을"</b>이다. '
    '강점은 (지치지 않는 열정), (끈질긴 호기심), (긍정)이다. '
    '지인들은 나에 대해 종종 (알파 에너지가 넘치는), (언제나 공부하고 연구하는), (쿨함)이라고 표현하곤 한다.',
    s_example))

story.append(divider())
story.append(Paragraph('✦ 내 작성 — My Story', s_caption))
story.append(Paragraph(
    '성인이 되기 전, 내가 가장 행복했던 한 장면을 떠올려보라고 하면 <b>학교가 끝나고 밤늦게까지 농구 코트에서 팀과 함께 뛰던</b> 순간이 가장 먼저 떠오른다. '
    '그 이유를 곰곰이 생각해보면 그것이 나에게 <b>몸이 먼저 반응하고 팀이 하나가 되는 순수한 몰입감</b>을 줬기 때문이다. '
    '성인이 된 후, 나에게 가장 큰 성취감을 안겨줬던 것은 <b>AI와 디자인을 결합해 나만의 방식으로 일하는 법을 발견</b>한 것이다. '
    '이때, 그 결과물을 떠나 <b>남들과 다른 방식으로 새로운 것을 발견하고 만들어낼 때</b> 나는 굉장한 기쁨을 느끼는 사람이라는 것을 알게 되었다. '
    '무엇보다 지금까지의 삶에서 내 가슴을 가장 뜨겁게 했던 순간을 꼽으라고 한다면 아마도 <b>샌디에고에서 아무런 틀 없이 다양한 나라 친구들과 자유롭게 살던</b> 것을 꼽을 것이다. '
    '왜냐하면 그때 <b>세상은 내가 상상하던 것보다 훨씬 넓고, 낯선 것이 위험이 아니라 가능성이라는 것</b>을 느끼고, 깨달았기 때문이다. '
    '이러한 경험들이 쌓이면서 아마도 내가 처음으로 꾸었던 꿈은 <b>과학자</b>이다. '
    '하지만 힘들었던 어떤 사건으로 인해 나는 오히려 <b>어떤 상황에서도 스스로 해결하는 힘이 내 안에 있다는 것</b>을 깨달으며, 내 삶에서 이것이 얼마나 중요한 지를 알게 되었다. '
    '이러한 다양한 경험들로 인해 인생의 좌우명이랄까, 그것은 <b>"경험할수록 더 많은 것을 느낀다. 실패하면 얻는 것이 많다. 내가 행복해야 한다."</b>이다. '
    '내가 생각하는 나의 강점 혹은 장점은 (추진력), (관찰력), (적응력)이다. '
    '그리고 내 주변의 지인들이 나에 대해 종종 말할 때 (도전적이다), (추진력있다)라고 나를 표현하곤 한다.',
    s_mine))
story.append(Paragraph(
    '나는 책이나 뉴스 등 어떤 새로운 정보를 접할 때 <b>사람과 인간관계</b>에 관한 내용에 항상 먼저 관심이 많이 간다. '
    '그 이유는 결국 모든 것의 중심에는 사람이 있고, 사람이 어떻게 살아가는지가 항상 궁금하기 때문이다. '
    '또한 나는 사람들을 만날 때 일상적인 대화 외에 관심을 가지며 던지는 주요 화두는 <b>"요즘 뭐가 즐거워?"</b>이다. '
    '그 이유는 나는 항상 그 사람이 살아있음을 느끼는 순간이 어디에 있는지가 궁금하기 때문이다. '
    '만약, 어떤 신문에서 나를 인터뷰하고 싶어 한다면, 나는 아마도 <b>\'경험이 사람을 어떻게 바꾸는가\'</b>라는 주제로 인터뷰에 응할 것이다. '
    '그 이유는 실패든 성공이든, 경험은 사람을 가장 깊이 성장시키는 힘이라고 믿기 때문이다.',
    s_mine))
story.append(Paragraph(
    '인생의 황혼기에 접어들었을 때 나는 주변 사람들로부터 <b>많은 경험으로 풍성하게 살았다</b>고 평가 받고 싶다. '
    '이러한 이야기를 듣기 위해 나는 오늘도 새로운 것에 도전하고 경험을 쌓기 위해 노력하고 있다.',
    s_mine))
story.append(Spacer(1, 10*mm))

# ── PART 3 ────────────────────────────────────────────
story.append(section_box('PART 3.  나를 3문장으로 정의하기'))
story.append(Spacer(1, 4*mm))

story.append(Paragraph('안내', s_label))
story.append(Paragraph(
    '여러분이 쓴 스토리 보드에서 당신이 어떤 형용사나 동사를 썼는지 살펴보세요. '
    '그 단어들을 찬찬히 곱씹어 보며, 당신을 세 개의 문장으로 한번 정의해보세요. '
    '먼저 한 줄의 문장으로 정의한 후, 그것을 단 하나의 단어로 압축해보세요!', s_body))

story.append(Spacer(1, 2*mm))
story.append(Paragraph('예시', s_label))
story.append(Paragraph('나는 불가능한 것에 도전하고 그것을 위해 기꺼이 열정을 쏟는 사람이다.  →  도전', s_example))

story.append(divider())
story.append(Paragraph('✦ 내 작성 — 3문장 정의', s_caption))
story.append(Paragraph('①  나는 사람을 관찰하고, 도전하고, 실패 속에서 나만의 방식을 찾아온 사람이다.', s_mine))
story.append(Paragraph('→  관찰', s_keyword))
story.append(Spacer(1, 3*mm))
story.append(Paragraph('②  막힌 길 앞에서 같은 방식을 고집하지 않고, 새로운 도구와 방법으로 계속 나아간다.', s_mine))
story.append(Paragraph('→  도전', s_keyword))
story.append(Spacer(1, 3*mm))
story.append(Paragraph('③  다양한 경험으로 풍성하게 살다 가는 것, 그것이 내가 추구하는 삶이다.', s_mine))
story.append(Paragraph('→  경험', s_keyword))
story.append(Spacer(1, 10*mm))

story.append(divider('#dddddd'))
story.append(Paragraph('Copyrightⓒ by Ore&project. ALL RIGHTS RESERVED.  |  작성자 개인 제출본', s_note))

doc.build(story)
print("PDF 생성 완료: 사전과제_작성본.pdf")
