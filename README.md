# Udemy - 100 days of code (Python)



## Day 1 ~ Day 100

- [x] Day 16 - Object Oriented Programming (OOP)

  21년 2월 6일 완료

- [x] Day 17 - The Quiz Project & the Benefits of OOP

  21년 2월 7일 완료

- [ ] Day 18 - 



## 간단한 메모



### Day 17

- 수업에서 제시한 순서대로 클래스를 하나하나 만들어 코드를 완성하였는데, 어떻게 클래스를 만들 수 있느냐 보다는 **클래스를 어떻게 설계하느냐**가 더 중요하진 않을까 생각이 들었다.
  이 개념을 까먹지 않고, 다른 수업을 들을 때에도 신경써가며 코드를 살펴보아야겠다.

- 마지막 강의에서는 [OPEN TRIVIA DB][https://opentdb.com/]에 있는 문제를 복사하여, 문제를 구성하는 것으로 코드를 일부 수정하였다. 나는 여기에서 조금 더 나아가, SSAFY에서 배웠던 `requests`모듈을 이용하여 문제를 바로 받아오는 것을 짜보았고, 그 코드는 다음과 같다.

  ```python
  import requests
  
  url = "https://opentdb.com/api.php?amount=10&type=boolean"
  
  response = requests.get(url)
  data = response.json()
  results = data.get("results", [])
  question_data = []
  for question in results:
      question["question"] = question["question"].replace("&quot;", "\"").replace("#039;", "\'")
      question_data.append(question)
  
  ```

  API를 통해 넘어오는 문제 텍스트에서 큰 따옴표와 작은 따옴표가 특수코드 형태로 넘어와 자동으로 변환되진 않았는데, 이를 해결하기 위해 순환하며 replace 메서드를 사용하여 문자열을 바꿔주었다.
  나중에는 더 나은 방법을 찾을 수 있을 것 같기도 한데, 오늘은 replace로 처리한 것으로 마무리하려고 한다.