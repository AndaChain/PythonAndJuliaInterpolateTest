using Plots
using Symbolics
# ******************* input function ******************* 
function fx(x)
    return @.cos(-x)^2/9.0
end
# *********************************************************

struct Interpolation{}
    result::Any
    function Interpolation(x, y, name)
        if(name == "linear")
            result = linear_function(x, y)
            return result
        elseif(name == "quadratic")
            result = quadratic_function(x, y)
            return result
        elseif(name == "cubic")
            result = cubic_function(x, y)
            return result
        else
            return result
        end
        
    end
end
# *********************************************************

function linear_function(x, y)
    @variables X
    result = []
    for i = 1:length(x)-1
        a1 = y[i] / (x[i] - x[i+1])
        a2 = y[i+1] / (x[i+1] - x[i])
        equ = (a1 * (X - x[i+1])) + (a2 * (X - x[i]))
        
        result = append!(result, [[equ, x[i], x[i+1]]])
    end
    return result
end
# *********************************************************

function quadratic_function(x, y)
        result = []
        @variables X
        a_initial = 0
        b_initial = 0
        for i = 2:1:length(x)
            if(i == 2)
                matrix_A = [ [x[i-1] 1]; [x[i] 1] ]
                matrix_B = [ y[i-1], y[i] ]
                output = matrix_A\matrix_B
                
                b_initial = output[1]
                equation = (b_initial*X) + output[2]
                result = append!(result, [ [equation, x[i - 1], x[i]] ])
            elseif(i == 3)
                row1 = [2*x[i - 1]  1  0]
                row2 = [(x[i - 1])^2  x[i - 1]  1]
                row3 = [(x[i])^2  x[i]  1]
                
                matrix_A = [row1; row2; row3]
                matrix_B = [b_initial, y[i-1], y[i]]
                output = matrix_A\matrix_B
                
                a_initial = output[1]
                b_initial = output[2]
                equation = (a_initial * (X^2)) + (b_initial*X) + output[3]
                result = append!(result, [ [equation, x[i - 1], x[i]] ])
            else
                row1 = [2*x[i - 1]  1  0]
                row2 = [(x[i - 1])^2  x[i - 1]  1]
                row3 = [(x[i])^2  x[i]  1]
                
                matrix_A = [row1; row2; row3]
                matrix_B = [(2*a_initial*x[i-1])+b_initial, y[i-1], y[i]]
                output = matrix_A\matrix_B
                
                a_initial = output[1]
                b_initial = output[2]
                equation = (a_initial*(X^2)) + (b_initial*X) + output[3]
                result = append!(result, [ [equation, x[i - 1], x[i]] ])
            end
        end
        return result
end
# *********************************************************

function cubic_function(x, y)
        i = 3
        if(length(x) > 2)
            i = length(x)-1
        end
        _k = zeros(Float64, i-1, i-1)
        matrix_k = collect(eachrow(_k))

        _y = zeros(Float64, i-1, 1)
        matrix_y = collect(eachrow(_y))

        for row = 2:1:i
	        for col = 2:1:i
	            if(row == col)
	                diagonal = col - 1
	                matrix_k[diagonal][diagonal] = 4
	                if(diagonal - 1 >= 1)
	                    matrix_k[diagonal][diagonal - 1] = 1
                    end
	                if(diagonal + 1 < length(matrix_k[diagonal])+1)
	                    matrix_k[diagonal][diagonal + 1] = 1
                    end
	                Y = y[diagonal] - 2 * y[diagonal+1] + y[diagonal + 2]
	                X = 6 / (x[diagonal+1] - x[diagonal])^2
	                matrix_y[row-1][1] = X*Y
                    
                end
            end
        end
        
        output = _k\_y
        
        result = []
        @variables X
        
        for _i = 1:1:i
            if(_i == 1)
                k1 = 0
                k2 = output[_i]
                equation = equ(X, x, y, k1, k2, _i)
                result = append!(result, [ [equation, x[_i], x[_i + 1]] ])
            elseif(_i == i)
                k1 = output[_i - 1]
                k2 = 0
                equation = equ(X, x, y, k1, k2, _i)
                result = append!(result, [ [equation, x[_i], x[_i + 1]] ])
            else
                k1 = output[_i - 1]
                k2 = output[_i]
                equation = equ(X, x, y, k1, k2, _i)
                result = append!(result, [ [equation, x[_i], x[_i + 1]] ])
            end
        end
        return result
        
end
# *********************************************************

function equ(X, x, y, k1, k2, _i)
	    equation_1 = (k1 / 6) * (
			(  ((X - x[_i + 1]) ^ 3) / (x[_i] - x[_i + 1]))
			- ((X - x[_i + 1]) * (x[_i] - x[_i + 1]))
		)
	    equation_2 = (k2 / 6) * (
			(  ((X - x[_i]) ^ 3) / (x[_i] - x[_i + 1])) - ((X - x[_i]) * (x[_i] - x[_i + 1]))
		)
	    equation_3 = (y[_i] * (X - x[_i + 1]) - y[_i + 1] * (X - x[_i])) / (
			x[_i] - x[_i + 1]
		)
	    equation_full = equation_1 - equation_2 + equation_3
	    return equation_full
end
# *********************************************************

function set_x(result, x)
    @variables X
    y = []
    for i in x
        for j in result
            if(j[2] <= i <= j[3])
                f = j[1]
                answer = Symbolics.value.( substitute.(f, (Dict(X => i),) )[1] )
                y = append!(  y, [answer]  )
                break
            end
        end
    end
    return y
end
# *********************************************************

function set_graph()
    width, height = 640, 480 # width and height of canvas
    plot!(size = (width, height), reuse=false)
    plot!(legend = :bottomleft, reuse=false)
    current_dir = pwd()*"\\DIY_julia.png"
    savefig(current_dir)
    
end
# *********************************************************

function linspace(start,stop,num)
    x = []
    step = (stop-start)/num
    ma = start
    for i in start:step:stop
        x = append!(x, [i])
        if(ma < i)
            ma = i
        end
    end
    if(ma < stop)
        x = append!(x, [stop])
    end
    
    return x
end
# *********************************************************

function main(start, stop, N)
    x = linspace(start,stop,N)
    x_new = linspace(start,stop,N*10) #start:step*0.1:stop
    println(start,"\t",stop)
    y = fx(x)
    
    t1_S = time_ns()
    linear = Interpolation(x,y,"linear")
    t1_E = time_ns()
    if((t1_E-t1_S)*10^-9 < 0.000001)
        t1 = "It's less than 1 us"
    else
        t1 = string(round((t1_E-t1_S)*10^-9, digits=6))
    end
    y_linear = set_x(linear, x_new) # use this to interpolation

    t2_S = time_ns()
    quadratic = Interpolation(x,y,"quadratic")
    t2_E = time_ns()
    if((t2_E-t2_S)*10^-9 < 0.000001)
        t2 = "It's less than 1 us"
    else
        t2 = string(round((t2_E-t2_S)*10^-9, digits=6))
    end
    y_quadratic = set_x(quadratic, x_new) # use this to interpolation

    t3_S = time_ns()
    cubic = Interpolation(x,y,"cubic")
    t3_E = time_ns()
    if((t3_E-t3_S)*10^-9 < 0.000001)
        t3 = "It's less than 1 us"
    else
        t3 = string(round((t3_E-t3_S)*10^-9, digits=6))
    end
    y_cubic = set_x(cubic, x_new) # use this to interpolation

    println(t1)

    println(t2)

    println(t3)

    open("time_DIY.csv", "w") do io
        write(io, "Linear,Quadratic,Cubic\n")
        write(io, t1,",",t2,",",t3)
    end;
    
    scatter(x, y, markersize=10,label="Data points")
    plot!(x_new, y_linear, w=3,label="Linear interpolation", reuse=false)
    plot!(x_new, y_quadratic, linestyle=:dash, w=3, label="Quadratic interpolation", reuse=false)
    plot!(x_new, y_cubic, w=3,label="Cubic interpolation", reuse=false)
    set_graph()

end
# *********************************************************

if abspath(PROGRAM_FILE) == @__FILE__
    start = 1
    stop =  10
    N = 5
    main(start, stop, N)
end