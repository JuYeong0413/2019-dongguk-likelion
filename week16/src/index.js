import "./styles.css";

document.getElementById("app").innerHTML = `
<h1>Hello Vanilla!</h1>
<div>
  We use Parcel to bundle this sandbox, you can find more info about Parcel
  <a href="https://parceljs.org" target="_blank" rel="noopener noreferrer">here</a>.
</div>
`;

let value = 1;
// 같은 이름으로 변수 선언 불가능
console.log(value);

value = 5;
console.log(value);
// 값은 변경 가능

var hello = "hello";
// 구석기 시대의.. 방식.. 써도 괜찮은데... 돌아가긴 하는데 지양할 것

const v = 3;
console.log(v);
// const는 상수 -> 바뀌면 안되는 값

let val = 1;
val = "hello ";
let val2 = "nihao";
console.log(val + val2);

const stringSum = "hello : " + val2;
console.log(stringSum);

// template literal 문자열 안에 변수를 집어넣을 수 있는 문법
const stringS = `hello : ${val2}`;
console.log(stringS);

// Boolean
let b = false;

// Array
const animals = ["멍멍이", "고양이", true];
console.log(animals);

// Object
const person = {
  name: "주영",
  age: 23
};
console.log(person.name);

// Null
// null은 없는 것 undefined는 알 수 없음
let friends = null;
let criminal = undefined;
let c;
console.log(c); // undefined

// ! 부정
let result2 = !true;
console.log(result2);

// 비교 연산자
// == 형 검사 안함
let va1 = "1";
let va2 = 1;
let va3 = true;
console.log(va1 == va2);
console.log(va3 == va2);
// === 자료형까지 같은지 검사함
// javascript는 무조건 등호 3개를 쓴다고 생각해도 됨
console.log(va3 === va2);

console.log(va3 !== va2);

const cat = {
  sound: "짹짹",
  age: 3
};

if (cat.sound === "야옹") {
  console.log("고양이 입니다.");
} else if (cat.sound === "멍멍") {
  console.log("멍멍이 입니다.");
} else {
  console.log("??");
}

// 함수
// 반환하는 함수
function add(a, b) {
  return a + b;
}

const sum = add(2, 3);
console.log(sum);

// 실행하는 함수
function helloName(name) {
  // console.log("hello : " + name);
  console.log(`hello ${name}!`);
}

helloName("juyeong");
