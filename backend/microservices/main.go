package main

import (
	"fmt"
)

type kelvin float64
type celsius float64
type activator bool

func (k kelvin) celsius() celsius {
	return celsius(k - 273.15) // convert float64 to celsius
}

func (c celsius) kelvin() kelvin {
	return kelvin(c + 273.15) // convert float64 to kelvin
}

func (a activator) activator() activator {
	a = true
	return a
}

func make_yandex_man() bool {
	return true
}

func main() {
	var arr = []int{}
	fmt.Println(arr)

}
