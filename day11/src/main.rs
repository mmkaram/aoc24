use std::collections::HashMap;
use std::f64;

fn digit_count(n: u64) -> u64 {
    if n == 0 {
        return 1;
    }
    (n as f64).log10().floor() as u64 + 1
}

fn powers_of_10() -> Vec<u64> {
    (0..20).map(|i| 10u64.pow(i)).collect()
}

fn blink(stones: Vec<u64>, memo: &mut HashMap<u64, Vec<u64>>, powers_of_10: &[u64]) -> Vec<u64> {
    let mut ret = Vec::new();

    for &i in &stones {
        let x = digit_count(i);

        if let Some(cached) = memo.get(&i) {
            ret.extend(cached.iter().copied());
        } else if i == 0 {
            ret.push(1);
            memo.insert(i, vec![1]);
        } else if x % 2 == 0 {
            let power = (x / 2) as usize;
            let first_part = i / powers_of_10[power];
            let second_part = i % powers_of_10[power];
            ret.push(first_part);
            ret.push(second_part);
            memo.insert(i, vec![first_part, second_part]);
        } else {
            let transformed = 2024 * i;
            ret.push(transformed);
            memo.insert(i, vec![transformed]);
        }
    }

    ret
}

fn part_one(data: &str) -> usize {
    let mut x: Vec<u64> = data
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let mut memo = HashMap::new();
    let powers_of_10 = powers_of_10();

    for _ in 0..25 {
        x = blink(x, &mut memo, &powers_of_10);
    }

    x.len()
}

fn part_two(data: &str) -> usize {
    let mut x: Vec<u64> = data
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let mut memo = HashMap::new();
    let powers_of_10 = powers_of_10();

    for i in 0..75 {
        x = blink(x, &mut memo, &powers_of_10);
        if i % 10 == 0 {
            println!("Iteration: {}", i);
        }
    }

    x.len()
}

fn main() {
    let data = "1 2 3 4 5";
    println!("Part Two Result: {}", part_two(data));
}
