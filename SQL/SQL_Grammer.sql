[SELECT문 구성]

SELECT 가져올 컬럼들 FROM 참조할 테이블명 [WHERE 조건] [ORDER BY ASC(오름차순), DESC(내림차순)] [GROUP BY 묶어서 보여줄 컬럼명]

[GROUP BY]

SELECT [ ALL | DISTINCT ] 속성_리스트
FROM 테이블_리스트
[ WHERE 조건 ]
[ GROUP BY 속성_리스트 [ HAVING 조건 ] ]
[ ORDER BY 속성_리스트 [ ASC | DESC ] ];

[JOIN] *** 가장 중요

관계형 데이터베이스에서 테이블 간의 결합
1. 이너조인
 조인하고자 하는 두 개의 테이블에서 공통된 요소들을 통해 결합하는 조인방식

2. 레프트조인
 왼쪽에는 모두 있고 왼쪽 오른쪽 모두 있는거 합침