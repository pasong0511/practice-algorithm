process.stdin.setEncoding('utf8');

process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    //console.log(a);
    //console.log(b);
    
    let star = ''
    for (let i = 0; i<b; i++) {
        for (let j = 0; j<a; j++) {
            star += '*'
        }
        star += '\n'
    }
    console.log(star)
});



// n, m = map(int, input().strip().split(' '))

// for i in range(m) :
//     for j in range(n) : 
//         print("*", end="")
//     print()