//
//  ContentView.swift
//  Unit Convertor
//
//  Created by Dhruv Khanna on 28/03/23.
//

import SwiftUI

struct ContentView: View {
    @State private var inputValue = 0.0
    @FocusState private var inputIsFocused : Bool
    @State private var conversion : String = "Temperature"
    @State private var inpUnit : String = "None"
    @State private var outUnit : String = "None"
    
    let conversions = ["Temperature", "Length", "Time", "Volume"]
    
    var unitList : [String] {
        switch conversion {
        case "Temperature":
            return ["C", "F", "K"]
        case "Length":
            return ["m", "km", "ft", "yd", "mi"]
        case "Time":
            return ["sec", "min", "hrs", "days"]
        case "Volume":
            return ["ml", "l", "pt", "gal", "cups"]
        default:
            return ["Error"]
        }
    }
    
    var answer : Double {
        switch conversion{
        case "Temperature":
            switch inpUnit {
            case "C":
                switch outUnit {
                case "C":
                    return inputValue
                case "F":
                    return inputValue*9/5 + 32
                case  "K":
                    return inputValue + 273.15
                default:
                    return 0.0
                }
            case "F":
                switch outUnit {
                case "C":
                    return 5*(inputValue-32)/9
                case "F":
                    return inputValue
                case  "K":
                    return 5*(inputValue-32)/9 + 273.15
                default:
                    return 0.0
                }
            case  "K":
                switch outUnit {
                case "C":
                    return inputValue - 273.15
                case "F":
                    return (inputValue - 273.15)*9/5 + 32
                case  "K":
                    return inputValue
                default:
                    return 0.0
                }
            default:
                return 0.0
            }
            
        case "Length":
            switch inpUnit {
            case "m":
                switch outUnit {
                case "m":
                    return inputValue
                case "km":
                    return inputValue / 1000
                case "ft":
                    return inputValue * 3.28084
                case "yd":
                    return inputValue * 1.0936133333333
                case "mi":
                    return inputValue * 0.00062137121212119323429
                default:
                    return 0.0
                }
            case "km":
                switch outUnit {
                case "m":
                    return inputValue * 1000
                case "km":
                    return inputValue
                case "ft":
                    return inputValue * 3280.8399999999001011
                case "yd":
                    return inputValue * 1093.6133333333000337
                case "mi":
                    return inputValue * 0.62137121212119317271
                default:
                    return 0.0
                }
            case "ft":
                switch outUnit {
                case "m":
                    return inputValue * 0.30480000975359072823
                case "km":
                    return inputValue * 0.00030480000975359071219
                case "ft":
                    return inputValue
                case "yd":
                    return inputValue * 0.333333
                case "mi":
                    return inputValue * 0.000189394
                default:
                    return 0.0
                }
            case "yd":
                switch outUnit {
                case "m":
                    return inputValue * 0.9144
                case "km":
                    return inputValue * 0.0009144
                case "ft":
                    return inputValue * 3
                case "yd":
                    return inputValue
                case "mi":
                    return inputValue * 0.000568182
                default:
                    return 0.0
                }
            case "mi":
                switch outUnit {
                case "m":
                    return inputValue * 1609.34
                case "km":
                    return inputValue * 1.60934
                case "ft":
                    return inputValue * 5280
                case "yd":
                    return inputValue * 1760
                case "mi":
                    return inputValue
                default:
                    return 0.0
                }
            default:
                return 0.0
            }
            
        case "Time":
            switch inpUnit {
            case "sec":
                switch outUnit {
                case "sec":
                    return inputValue
                case "min":
                    return inputValue * 0.0166667
                case "hrs":
                    return inputValue * 0.000277778
                case "days":
                    return inputValue * 0.0000115741
                default:
                    return 0.0
                }
            case "min":
                switch outUnit {
                case "sec":
                    return inputValue * 60
                case "min":
                    return inputValue
                case "hrs":
                    return inputValue * 0.0166667
                case "days":
                    return inputValue * 0.000694444
                default:
                    return 0.0
                }
            case "hrs":
                switch outUnit {
                case "sec":
                    return inputValue * 3600
                case "min":
                    return inputValue * 60
                case "hrs":
                    return inputValue
                case "days":
                    return inputValue * 0.0416667
                default:
                    return 0.0
                }
            case "days":
                switch outUnit {
                case "sec":
                    return inputValue * 86400
                case "min":
                    return inputValue * 1440
                case "hrs":
                    return inputValue * 24
                case "days":
                    return inputValue
                default:
                    return 0.0
                }
            default:
                return 0.0
            }
            
        case "Volume":
            switch inpUnit {
            case "ml":
                switch outUnit {
                case "ml":
                    return inputValue
                case "l":
                    return inputValue * 0.001
                case "pt":
                    return inputValue * 0.00211338
                case "gal":
                    return inputValue * 0.000264172
                case "cups":
                    return inputValue * 0.00416667
                default:
                    return 0.0
                }
            case "l":
                switch outUnit {
                case "ml":
                    return inputValue * 1000
                case "l":
                    return inputValue
                case "pt":
                    return inputValue * 2.11338
                case "gal":
                    return inputValue * 0.264172
                case "cups":
                    return inputValue * 4.16667
                default:
                    return 0.0
                }
            case "pt":
                switch outUnit {
                case "ml":
                    return inputValue * 473.176
                case "l":
                    return inputValue * 0.473176
                case "pt":
                    return inputValue
                case "gal":
                    return inputValue * 0.125
                case "cups":
                    return inputValue * 1.97157
                default:
                    return 0.0
                }
            case "gal":
                switch outUnit {
                case "ml":
                    return inputValue * 3785.41
                case "l":
                    return inputValue * 3.78541
                case "pt":
                    return inputValue * 8
                case "gal":
                    return inputValue
                case "cups":
                    return inputValue * 15.7725
                default:
                    return 0.0
                }
            case "cups":
                switch outUnit {
                case "ml":
                    return inputValue * 240
                case "l":
                    return inputValue * 0.24
                case "pt":
                    return inputValue * 0.50721
                case "gal":
                    return inputValue * 0.0634013
                case "cups":
                    return inputValue
                default:
                    return 0.0
                }
            default:
                return 0.0
            }
        default:
            return 0.0
        }
    }
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    Picker("Conversion Unit", selection: $conversion) {
                        ForEach(conversions, id: \.self) {
                            Text($0)
                        }
                    }
                } header: {
                    Text("Choose the unit conversion")
                }
                
                
                Section {
                    Picker("\(conversion) Unit", selection: $inpUnit) {
                        ForEach(unitList, id: \.self) {
                            Text($0)
                        }
                    }
                    .pickerStyle(.segmented)
                    
                    TextField("Convert from", value: $inputValue, format: .number)
                        .keyboardType(.decimalPad)
                        .focused($inputIsFocused)
                    } header: {
                    Text("Convert From")
                }
                
                
                Section {
                    Picker("\(conversion) Unit", selection: $outUnit) {
                        ForEach(unitList, id: \.self) {
                            Text($0)
                        }
                    }
                    .pickerStyle(.segmented)
                    
                    Text("\(answer.formatted())")
                } header: {
                    Text("Convert to")
                }
            }
            .navigationTitle("Ease Unit")
            .toolbar {
                ToolbarItemGroup(placement: .keyboard) {
                    Spacer()
                    
                    Button("Done") {
                        inputIsFocused = false
                    }
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
