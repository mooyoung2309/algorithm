//
//  main.swift
//  Swift
//
//  Created by 송영모 on 2022/04/14.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let a = input[0]
let b = input[1]

print(a + b)
