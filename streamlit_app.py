import os
import streamlit as st
import anthropic
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 가져오기 및 확인
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    st.error("API 키가 설정되지 않았습니다. .env 파일에 ANTHROPIC_API_KEY를 설정해주세요.")
    st.stop()

# Claude API 클라이언트 초기화
client = anthropic.Anthropic(api_key=api_key)

# Streamlit 앱 설정
st.title("신입사원 회사 생활 가이드")

# 회사 정보 (Instructions)
company_info = """
# (가상) 필로소피 AI 교육 신입사원 안내서

안녕하세요, 필로소피 AI 교육의 새로운 가족이 되신 것을 진심으로 환영합니다! 이 안내서는 여러분의 원활한 회사 생활 적응을 돕기 위해 작성되었습니다.

## 1. 회사 소개

필로소피 AI 교육은 인공지능 기술을 활용한 혁신적인 교육 솔루션을 제공하는 기업입니다. 우리의 미션은 "AI로 모두에게 맞춤형 교육을"입니다.

- 설립년도: 2020년
- 대표이사: OOO
- 주요 서비스: AI 튜터링 시스템, 맞춤형 학습 콘텐츠 제작, 교육기관 AI 솔루션 제공

## 2. 근무 환경

- 근무시간: 평일 09:00 - 18:00 (점심시간 12:00 - 13:00)
- 근무형태: 주 5일 근무, 유연근무제 시행 중
- 위치: 서울특별시 강남구 테헤란로 123 필로소피타워 15층

## 3. 복리후생

- 4대 보험
- 연차휴가 및 경조사 휴가
- 생일 반차
- 점심 식대 지원
- 자기계발비 지원 (월 10만원)
- 업무 관련 도서 구입비 지원

## 4. 주요 부서 및 연락처

- 인사팀: hr@philosophyai.kr / 내선 1001
- IT지원팀: it@philosophyai.kr / 내선 1002
- 재무팀: finance@philosophyai.kr / 내선 1003
- 고객지원센터: support@philosophyai.kr / 내선 1004

## 5. 회사 문화

- 수평적 조직 문화: 직급에 관계없이 서로 '님'으로 호칭
- 주간 전체 회의: 매주 월요일 오전 10시
- 분기별 타운홀 미팅: 분기마다 마지막 주 금요일 오후 4시
- 혁신의 날: 매월 마지막 주 수요일은 자유롭게 새로운 아이디어를 탐구하고 발표하는 날

## 6. 신입사원 교육 프로그램

- 오리엔테이션: 입사 첫날 (회사 소개, 규정 안내, 시스템 사용법 등)
- 멘토링 프로그램: 3개월간 선배 사원과 1:1 멘토링
- AI 기초 교육: 2주간의 집중 교육 프로그램

## 7. 주요 규정 및 에티켓

- 보안: 회사 내 정보 보안을 철저히 지켜주세요.
- 복장: 비즈니스 캐주얼을 기본으로 하되, 고객 미팅 시 정장 착용
- 회의실 사용: 회의실 예약 시스템을 통해 사전 예약 필수
- 커뮤니케이션: 업무용 메신저(Slack) 활용 권장

## 8. 성장 기회

- 분기별 성과 리뷰 및 피드백
- 연 1회 직무 역량 강화 워크샵
- 국내외 AI 교육 컨퍼런스 참가 지원

필로소피 AI 교육에서의 여러분의 새로운 시작을 다시 한 번 환영합니다. 궁금한 점이 있으시면 언제든 인사팀으로 문의해 주세요. 함께 성장하고 혁신할 수 있기를 기대합니다!
"""

# 사용자 입력 받기
user_question = st.text_input("회사에 대해 궁금한 점을 물어보세요:")

if user_question:
    # Claude에게 질문하기
    response = client.completions.create(
        model="claude-2",
        prompt=f"{company_info}\n\nHuman: {user_question}\n\nAssistant:",
        max_tokens_to_sample=300,
    )
    
    # 응답 표시
    st.write("답변:", response.completion)

# 추가 기능을 위한 공간
st.sidebar.title("추가 정보")
st.sidebar.info("여기에 회사 로고나 추가 링크를 넣을 수 있습니다.")
