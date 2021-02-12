# Udemy - 100 days of code (Python)

## Day 1 ~ Day 100

- [x] Day 16 - Object Oriented Programming (OOP) [21/02/06]

- [x] Day 17 - The Quiz Project & the Benefits of OOP [21/02/07]

- [x] Day 18 - Turtle & the Graphical User Interface (GUI) [21/02/11]

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



---

### Day 18

- Turtle 클래스를 이용해 여러가지 요소를 그려보는 예제를 수행했다.

- 함수를 만들어 예제를 해결할 수도 있지만, SSAFY에서 배웠던 클래스 상속을 이용해 코드를 작성해보았다.

  1. 예제 4 - Draw a Random Walk

     ```python
     class MyTurtle(turtle.Turtle):
         def __init__(self):
             super().__init__()
             self.color_list = ["navy", "green", "orange red", "coral1", "peach puff", "cornsilk4", "DeepPink", "DarkViolet", "DeepSkyBlue"]

         def random_color(self):
             self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

         def random_walk(self, count, length):
             angle_list = [0, 90, 180, 270]
             for _ in range(count):
                 self.random_color()
                 self.setheading(random.choice(angle_list))
                 self.forward(length)
     ```

     - 색상을 담은 `color_list`를 클래스의 인스턴스 변수로 담는 코드
     - Turtle 클래스를 상속 받으며, `__init__`에서 인스턴스 변수를 생성할 때 부모 클래스의 생성자 함수도 실행하기 위해 `self().__init__()`을 하였다.

  2. 예제 5 - Draw a Spirograph

     ```python
     class MyTurtle(turtle.Turtle):
         def set_random_color(self):
             self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

         def spiro_graph(self, size_of_gap):
             count = 360 / size_of_gap
             for _ in range(int(count)):
                 self.right(size_of_gap)
                 self.set_random_color()
                 self.circle(100)
     ```

     - 거북이의 색상을 랜덤하게 변경하는 인스턴스 메서드인 `set_random_color`를 만들어, spiro graph를 그리는 인스턴스 메서드인 `spiro_graph` 내부에서 사용해보았다.



---

### Day 19 - Turtle Race

#### 😊 활동 내용

1. **Challenge 1** - 스크린 이벤트를 활용해 직접 turtle을 조작하기
2. **Challenge 2** - Turtle 클래스를 이용해 여러 인스턴스(Object)를 만들어, 경주 구현하기



#### 🤓 한 걸음 더

##### Challenge 1

1. 클래스 생성하기

   Challenge 1에서 작성한 코드는 거북이 한 마리에 대해서만 동작하게 되는데, Turtle 클래스를 상속받아 별도의 클래스를 만들면 여러 독립적인 거북이에게 기능을 적용할 수 있을 것이라는 생각에 `Challenge 1-1.py`을 작성하였다.

   생성한 함수 중 `reset`이라는 이름의 함수가 있었는데, 그 안에서 reset()을 호출하고 있어서 `recursion Error`가 발생하였다.

   함수 이름을 바꿔주어 에러를 해결하였다.

2. 이벤트 추가하기

   이동 및 초기화 외에 랜덤하게 색상을 변경하는 이벤트와 이전 시간에 했던 spirograph를 만드는 이벤트를 추가하였다.



##### Challenge 2

1. 클래스 생성하기

   거북이를 생성할 때, 초기화 하는 요소 중 겹치는 부분이 많아 Turtle 클래스를 상속받는 클래스를 생성해보았다.

   ```python
   class RacingTurtle(turtle.Turtle):
       def __init__(self, x, y, color):
           super().__init__()
           self.shape("turtle")
           self.color(color)
           self.penup()
           self.goto(x=x, y=y)
           self.is_race_on = True
   
       def random_forwards(self):
           self.forward(random.randint(0, 10))
   
       def is_race_over(self):
           if self.xcor() > 230:
               return True
   ```

   - 생성하고 보니, 큰 이점은 없는 것 같았다.

   - `is_race_on` 을 클래스 변수로 담고, 한 거북이의 레이스가 종료되었을 때 `self.scor() < 230`  `is_race_on`을 False로 변화시켜 모든 거북이가 멈추도록 하고 싶었지만, 한 함수에서 클래스 변수와 인스턴스 변수가 함께 사용되어야 하는 경우가 발생하여 이 방법은 사용하지 않는 것으로 하였다.

     이 때문에, 게임 관련 코드는 Challenge 2와 큰 차이가 없었다.

#### 🙄 마무리

- higher order function에 대해 알 수 있었고, 함수의 리턴값을 인자로 전달하는 것과 함수 그 자체를 전달하는 것의 차이에 대해 다시 한 번 확인할 수 있었다.

- 클래스를 생성하고 상속받는 것에 점차 익숙해지고 있다. 활용성은 좀 떨어질 수 있지만, 꾸준히 만들어보며 잊지 않도록 해야겠다.







