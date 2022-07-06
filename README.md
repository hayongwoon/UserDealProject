# 중고 거래 PROJECT
해당 플랫폼은 기존의 중고 거래 사이트와 유사합니다. 사용자는 중고 물품을 등록(게시)하여 구매자와 소통 후 직접 거래할 수 있게 하는 중계 플랫폼이며, 판매가 이루어진 후 판매자는 사용자에게 거래 완료 요청을 보낸다. 요청받은 구매자는 수락 후 판매자의 신뢰도 점수를 평가할 수 있다.
사용자의 거래 신뢰도에 따라 permission을 커스텀 할 예정이다.

## MODEL
- user
    - ID, 전화번호, 비밀번호, 이름, 가입일, 신뢰도, 활동여부, 관심 목록
        
- product
    - 작성자, 제목, 내용, 이미지, 카테고리, 좋아요 수

- product_comment
    - 상품, 작성자, 내용

- success_deal
    - 판매자, 구매자, 상품, 거래 만족도(신뢰도) 점수

- product_like
    - 사용자, 상품


## VEIW
- user
    - 사용자의 신뢰도 점수가 있고, 거래가 끝나면 구매한 사용자가 판매한 사용자에게 점수를 부여
    - 신뢰도는 5점 만점으로 거래를 하면서 구매자에게 평점을 얻는다. 해당 점수를 통해 permission을 커스텀 할 예정 ex) 신뢰도가 2점 이하인 사람은 상품 등록 거부.
    - 관심 목록에 따른 상품 추천

- product
    - 상품 등록, 상품 조회(등록 순), 상품 삭제, 상품 업데이트
    - 사용자가 판매 중인 모든 품목 조회

- like(장바구니)
    - 상품 찜 등록, 취소

- comment
    - 상품에 댓글 생성, 수정, 삭제, 조회

- success_deal
    - 거래가 완료되면 판매자는 구매자에게 거래 완료 요청을 보내고 구매자는 요청 수락 후 판매자 신뢰도 점수 부여 거래가 완료 된다면, 상품의 is_active=False 로 바꾼다. 


