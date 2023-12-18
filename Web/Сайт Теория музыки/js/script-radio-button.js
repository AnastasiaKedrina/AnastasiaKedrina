var check1,check2;
function radioClick(c) {
    if (check1 != c) {
        check2 = 0;
        check1 = c
    }
    check2 ^= 1;
    c.checked = check2
}