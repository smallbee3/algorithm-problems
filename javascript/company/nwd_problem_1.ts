// 12:34pm
// 01:20pm

const shortestPath = (num, cur) => {
  let count = 0;
  const route = [2, 5, 8, 0];

  const curToDes = {
    1: 2,
    4: 5,
    7: 8,
    '*': 0,
    3: 2,
    6: 5,
    9: 8,
    '#': 0,
  };

  console.log({ num })
  console.log(1, { cur });

  if ([2, 5, 8, 0].indexOf(cur) < 0) {
    count += 1;
    cur = curToDes[cur];

  }
  console.log(2, { cur });

  let result = route.indexOf(cur) - route.indexOf(num);
  if (result < 0) result *= -1;
  console.log('result:', result + count);

  return result + count;
};

function solution(numbers, hand) {
  let answer = '';
  let curLeft = '*';
  let curRight = '#';

  for (const num of numbers) {
      console.log('start: ', num)
    if ([1, 4, 7].indexOf(num) > -1) {
      answer += 'L';
      curLeft = num;
    } else if ([3, 6, 9].indexOf(num) > -1) {
      answer += 'R';
      curRight = num;
    } else {
      console.log('left')
      const leftPath = shortestPath(num, curLeft);
      console.log('right')
      const rightPath = shortestPath(num, curRight);

      if (leftPath < rightPath) {
        answer += 'L';
        curLeft = num;
      } else if (leftPath > rightPath) {
        answer += 'R';
        curRight = num;
      } else {
        if (hand === 'left') {
          answer += 'L';
          curLeft = num;
        } else {
          answer += 'R';
          curRight = num;
        }
      }
    }
  }

  return answer;
}

let answer1 = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left');
console.log(answer1);
// 출력값: LRLLRRLLLRR

let answer2 = solution( [4, 1, 8, 7, 0, 2, 7, 3, 7, 1, 9], 'right' );
console.log( answer2 );
// // 출력값: LLRLRRLRLLR

let answer3 = solution( [8, 2, 0, 4, 2, 7, 6, 3, 5, 8, 2], 'left' );
console.log( answer3 );
// // 출력값: LLRLLLRRLLR
