// function fn(a, b) {
//     return a + b
// }
//
// console.log(fn(3, 5))
//
// function fn1(a) {
//     return a * 4
// }
//
// console.log(fn1(4))
//
//
// function fn2(a, b, c) {
//     return (a + b + c) / 3
// }
//
// console.log(fn2(2, 4, 6))
//
// function fn3() {
//     return 7
// }
//
// console.log(fn3())

// function fn4(a) {
//     return a % 5
// }
//
// console.log(fn4(10))

// function fn5(a, b) {
//     s = a + b
//     d = {'ch1': a, 'ch2': b, 'sum': s}
//     return d
// }
//
// console.log(fn5(4, 6))

// function fn6() {
//     a = parseInt(prompt("Введи число:"), 10)
//     if (a <= 34) {
//         console.log('oksana')
//     } else {
//         console.log('tanya')
//     }
// }
//
// console.log(fn6())

// function fn7() {
//     a = parseInt(prompt('введите 1ое число'), 10)
//     b = parseInt(prompt('введите 2ое число'), 10)
//     s = a + b
//     if (s == 5) {
//         console.log(5 / 2)
//     } else {
//         console.log(s)
//     }
// }
//
// console.log(fn7())

// function fn8(ls) {
//     sum = 0
//     for (var idx in ls)
//         {sum = sum + ls[idx]
//     } console.log(sum)
//
// }
//
// console.log(fn8([1, 2, 3, 4]))

// $(document).ready(function() {
//     $('#id22').click(function (e) {
//         alert('Кликните, чтобы узнать актуальную информацию об утилизации ЛС.')
//     })
//
// });
//
// $(document).ready(function() {
// $('#id111').click(function (e) {
//     window.location.pathname = '/patient'
// })
//
// });

$(document).ready(function () {
    $('#id111').click(function (e) {
        window.location.pathname = '/patient'
    })

});

$(document).ready(function () {
    $('#id555').click(function (e) {
        window.location.pathname = '/doctor'
    })

});

$(document).ready(function () {
    $('#id666').click(function (e) {
        window.location.pathname = '/farm'
    })

});

$(document).ready(function () {
    $('#id333').click(function (e) {
        window.location.pathname = '/about_us'
    })

});

$(document).ready(function () {
    $('#id222').click(function (e) {
        window.location.pathname = '/know'
    })

});