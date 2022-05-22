using Dierckx, Plots

# ******************* input function ******************* 
function fx(x)
    return @.cos(x^2/9.0)
end
# *********************************************************


# ******************* interpolate function ******************* 
function linear(x,y)
    return Spline1D(x, y; w=ones(length(x)), k=1, bc="nearest", s=0.0) # if k=1 then output as Linear Spline
end

function quadratic(x,y)
    return Spline1D(x, y; w=ones(length(x)), k=2, bc="nearest", s=0.0) # if k=2 then output as Quadratic Spline
end

function cubic(x,y)
    return Spline1D(x, y; w=ones(length(x)), k=3, bc="nearest", s=0.0) # if k=3 then output as Cubic Spline
end
# *********************************************************


# ******************* set graph ******************* 
function plot_graph(x, y, x_new)
    t1 = time_ns()
    f_linear = linear(x,y)
    t1 = time_ns()-t1
    
    t2 = time_ns()
    f_quadratic = quadratic(x,y)
    t2 = time_ns()-t2
    
    t3 = time_ns()
    f_cubic = cubic(x,y)
    t3 = time_ns()-t3
    
    print(t1)
    println(" ns")
    print(t2)
    println(" ns")
    print(t3)
    println(" ns")
    
    open("time_response.txt", "w") do io
        write(io, "Linear,Quadratic,Cubic\n")
        write(io, string(t1*10^-9),",",string(t2*10^-9),",",string(t3*10^-9))
    end;
    
    
    scatter!(x, y, markersize=10,label="Data points")
    plot!(x_new, fx(x_new), w=3,label="Real Data") # real function graph
    
    plot!(x_new, f_linear(x_new), w=3,label="Linear interpolation")
    plot!(x_new, f_quadratic(x_new), linestyle=:dash, w=3, label="Quadratic interpolation")
    plot!(x_new, f_cubic(x_new), linestyle=:dash, w=3, label="Cubic Spline interpolation")
end

function set_graph(x,y)
    width, height = 1000, 500 # width and height of canvas
    plot!(size = (width, height))
    xlims = (-4, 2)
    plot!(legend = :bottomleft)
    current_dir = pwd()*"\\plot_julia.png"
    savefig(current_dir)
end
# *********************************************************

function main(start, stop, N)
    step = (stop-start)/N
    x = start:step:stop
    x_new = start:step*0.01:stop
    y = fx(x)
    plot_graph(x, y, x_new)
    set_graph(x,y)
end
start = 1
stop =  10
N = 10
main(start, stop, N)
