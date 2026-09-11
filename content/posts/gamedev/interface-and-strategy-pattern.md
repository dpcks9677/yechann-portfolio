---
title: "유니티 C# | 인터페이스와 전략 패턴 (Strategy Pattern)"
date: "2026-09-11"
category: "유니티 C#"
description: "클래스나 구조체가 구현해야 하는 기능의 규약을 정의하는 키워드인 interface와, 실행 중에 알고리즘을 동적으로 변경할 수 있게 해주는 전략 디자인 패턴"
tags: ["Unity", "C#", "인터페이스", "디자인패턴", "Strategy"]
---

## 인터페이스 (interface)
클래스나 구조체가 구현해야 하는 기능의 규약(Contract)을 정의하는 키워드
- 메서드, 프로퍼티, 이벤트, 인덱서 등의 선언만 포함
- 원칙적으로 직접 인스턴스를 생성할 수 없음 (설계도의 개념이므로 직접 값을 저장하지 않음)

RPG 캐릭터를 만든다는 가정하에 다음과 같은 인터페이스를 작성한다.
```csharp
public interface ICharacter
{
    void Attack();
    void Heal();
    void TakeDamage(int damage);
}
```
캐릭터가 가지는 공통 기능을 메서드로 정의한다.
- 공격 (상대에게 피해를 입히는 기능)
- 회복 (자신의 HP를 올리는 기능)
- 피격 (데미지를 받았을 때 처리하는 기능)

이후 인터페이스를 상속하여 Warrior와 Mage를 각각 만든다.

*현재는 간단하게 구현하기 위해 텍스트를 표기하는 방식으로 구현한다.

```csharp
public class Warrior : ICharacter
{
    public void Attack()
    {
        Console.WriteLine("전사가 공격합니다.");
    }

    public void Heal()
    {
        Console.WriteLine("전사가 회복합니다.");
    }

    public void TakeDamage(int damage)
    {
        Console.WriteLine("전사가 데미지를 입습니다.");
    }
}
public class Mage : ICharacter
{
    public void Attack()
    {
        Console.WriteLine("마법사가 공격합니다.");
    }

    public void Heal()
    {
        Console.WriteLine("마법사가 회복합니다.");
    }

    public void TakeDamage(int damage)
    {
        Console.WriteLine("마법사가 데미지를 입습니다.");
    }
}
```

인터페이스를 받아서 클래스를 만드는 경우, 인터페이스에 구현된 메서드를 모두 선언해야만 에러없이 컴파일 된다. (하나라도 빼먹었다면 메서드가 구현이 되어 있지 않다고 알려준다.)
이 `interface` 키워드를 사용해서 다양한 디자인 패턴으로 확장할 수 있다.

## 전략 패턴 (Strategy)
실행 중에 알고리즘(행위)을 동적으로 변경할 수 있게 해주는 행동 디자인 패턴

- 전략 (Strategy): 알고리즘을 공통으로 선언하는 인터페이스 또는 추상 클래스
- 구체적인 전략 (Concrete Strategy): 전략 인터페이스를 실제로 구현한 개별 알고리즘 클래스입니다.
- 컨텍스트 (Context): 전략을 사용하는 주체. 전략 객체의 참조를 가지고 있으며, 필요에 따라 실행 중에 전략을 바꿀 수 있음.

런타임 중에 행동하는 방식을 바꿔야 하는 경우, 전략 패턴의 도입을 고려해볼 수 있다.
이번 예제에서는 여러가지 공격타입을 하나로 묶어서 표현하는 상황에서 코드를 기술하도록 하겠다.

우선 공통으로 가져야 할 점을 인터페이스로 분리한다. 공격이 기준이므로, 모든 상속될 클래스들은 `Attack()` 메서드를 구현해야만 한다. 매개변수로는 목표의 이름을 받는다.
```csharp
public interface IAttackStrategy
{
    void Attack(string monsterName);
}
```
그 다음에는 인터페이스에서 명시한 기능들을 각각의 클래스에 작성한다. 이 코드에서는 공격타입을 3가지를 작성한다. (검 공격, 활 공격, 마법 공격)

```csharp
// 검 공격 전략 (근접 단일 공격)
public class SwordAttack : IAttackStrategy
{
    public void Attack(string monsterName)
    {
        Console.WriteLine($"[검] ⚔️ {monsterName}에게 근접 베기 공격! (데미지: 50)");
    }
}

// 활 공격 전략 (원거리 단일 공격)
public class BowAttack : IAttackStrategy
{
    public void Attack(string monsterName)
    {
        Console.WriteLine($"[활] 🏹 {monsterName}에게 원거리 화살 발사! (데미지: 35)");
    }
}

// 마법 공격 전략 (범위 공격)
public class MagicAttack : IAttackStrategy
{
    public void Attack(string monsterName)
    {
        Console.WriteLine($"[마법] 🔥 {monsterName} 주변에 화염구(Fireball) 폭발! (데미지: 80)");
    }
}
```

다음으로, 해당 "전략"을 사용할 컨텍스트를 작성한다. `IAttackStrategy` 타입의 변수를 받을 수 있게 하는 것이 핵심이다.

```csharp
public class PlayerCharacter // 컨텍스트 클래스
{
    private string _name;
    private IAttackStrategy _attackStrategy; // 현재 장착된 무기(전략)

    public PlayerCharacter(string name)
    {
        _name = name;
    }

    // 장비 스왑(무기 교체)
    public void EquipWeapon(IAttackStrategy attackStrategy) // IAttackStrategy를 매개변수로 받아서 내용을 교체한다.
    {
        _attackStrategy = attackStrategy; // 선언 변수는 플레이어가 지니는 전략, 대입 변수는 매개변수로 받은 교체될 전략이다.
        Console.WriteLine($"[{_name}] 무기를 교체했습니다.");
    }

    // 공격 실행
    public void PerformAttack(string monsterName)
    {
        if (_attackStrategy == null)
        {
            Console.WriteLine($"[{_name}] 맨손으로 때릴 수는 없습니다! 무기를 장착하세요.");
            return;
        }

        Console.Write($"[{_name}] ");
        _attackStrategy.Attack(monsterName); // 장착된 전략의 Attack 호출
    }
}
```
---
### 장점
- <u>**OCP(개방-폐쇄 원칙)**</u> 준수: 기존 코드를 수정하지 않고도 새로운 전략(알고리즘)을 얼마든지 추가할 수 있음
- <u>**조건문(if-else, switch) 제거**</u>: 객체의 행동별로 조건문 분기를 복잡하게 늘어놓을 필요가 없어 코드가 깔끔해짐
- <u>**유연한 런타임 교체**</u>: 게임 실행 중에 전략이 바뀌면 내부 전략 객체만 교체(SetStrategy)하여 행동을 즉시 바꿀 수 있음
- <u>**코드 재사용성 및 단위 테스트 용이**</u>: 각 행동이 독립된 클래스로 캡슐화되어 있어, 특정 로직만 떼어내어 테스트하거나 다른 캐릭터에서 재사용할 수 있음

### 단점
- <u>**클래스 개수 증가**</u>: 행동 하나하나를 별도의 클래스로 생성해야 하므로, 관리해야 할 파일과 클래스의 수가 늘어나 구조가 다소 복잡해질 수 있음
- <u>**클라이언트의 이해도 필요**</u>: 객체를 사용하는 측(호출자)에서 다양한 전략들의 차이점을 알고, 적절한 전략을 직접 생성하여 주입해 주어야 함
- <u>**단순한 로직에는 과도한 설계(Overengineering)**</u>: 조건문 몇 줄로 끝날 간단한 동작 변경에 전략 패턴을 적용하면 오히려 불필요하게 코드가 복잡해짐
---
디자인 패턴을 오·남용 하는 것을 경계해야 한다고 하네요. 전략 패턴의 경우에도 마찬가지로 가짓수가 너무 많이 늘어나면 유지보수가 어려워지니 <u>**트레이드오프(trade-off)**</u>를 잘 해야합니다. 디자인 패턴은 일종의 공식 또는 해법이지, 절대적인 문제는 아닙니다. 저도 알맞는 디자인패턴을 잘 써보도록 노력해야겠어요.
