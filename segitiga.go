package main

import (
	"fmt"
	"math"
)

func isValid(a, b, c float64) bool { //arya
	// Jika ada sisi yang bernilai negatif atau nol
	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}

	// Jika sisi terbesar lebih besar atau sama dengan jumlah dua sisi lainnya
	if a+b <= c || a+c <= b || b+c <= a {
		return false
	}
	return true
}

func isApproximatelyEqual(a, b float64, tolerance float64) bool { //hilmi
	return math.Abs(a-b) <= tolerance*math.Min(a, b)
}

func isEquilateral(a, b, c float64, tolerance float64) bool { //akbar
	return isApproximatelyEqual(a, b, tolerance) && isApproximatelyEqual(b, c, tolerance)
}

func isIsosceles(a, b, c float64, tolerance float64) bool { //abizard
	return isApproximatelyEqual(a, b, tolerance) || isApproximatelyEqual(b, c, tolerance) || isApproximatelyEqual(a, c, tolerance)
}

func isRightTriangle(a, b, c float64, tolerance float64) bool { //arya
	// Memeriksa apakah memenuhi kondisi Pythagoras dengan toleransi
	return math.Abs(a*a+b*b-c*c) <= tolerance*math.Min(a*a+b*b, c*c) ||
		math.Abs(b*b+c*c-a*a) <= tolerance*math.Min(b*b+c*c, a*a) ||
		math.Abs(c*c+a*a-b*b) <= tolerance*math.Min(c*c+a*a, b*b)
}

func classifyTriangle(a, b, c float64) { //hilmi
	// Toleransi 1% (0,01)
	tolerance := 0.01

	// Validasi sisi segitiga
	if !isValid(a, b, c) {
		fmt.Println("Tidak ada segitiga yang dapat dibentuk.")
		return
	}

	// Klasifikasi segitiga
	if isEquilateral(a, b, c, tolerance) {
		fmt.Println("Segitiga Sama Sisi (Equilateral)")
	} else if isIsosceles(a, b, c, tolerance) {
		fmt.Println("Segitiga Sama Kaki (Isosceles)")
	} else if isRightTriangle(a, b, c, tolerance) {
		fmt.Println("Segitiga Siku-Siku (Right Triangle)")
	} else {
		fmt.Println("Segitiga Bebas (Scalene)")
	}
}

func main() {
	var a, b, c float64

	fmt.Print("Masukkan panjang sisi a: ")
	fmt.Scanln(&a)
	fmt.Print("Masukkan panjang sisi b: ")
	fmt.Scanln(&b)
	fmt.Print("Masukkan panjang sisi c: ")
	fmt.Scanln(&c)

	classifyTriangle(a, b, c)
}