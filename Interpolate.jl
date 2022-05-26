using Dierckx, Plots

# ******************* input function ******************* 
function fx(x)
    return @.cos(-x)^2/9.0
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
    t1_S = time_ns()
    f_linear = linear(x,y)
    t1_E = time_ns()
    if((t1_E-t1_S)*10^-9 < 0.000001)
        t1 = "It's less than 1 us"
    else
        t1 = string(round((t1_E-t1_S)*10^-9, digits=6))
    end

    t2_S = time_ns()
    f_quadratic = quadratic(x,y)
    t2_E = time_ns()
    if((t2_E-t2_S)*10^-9 < 0.000001)
        t2 = "It's less than 1 us"
    else
        t2 = string(round((t2_E-t2_S)*10^-9, digits=6))
    end
    
    t3_S = time_ns()
    f_cubic = cubic(x,y)
    t3_E = time_ns()
    if((t3_E-t3_S)*10^-9 < 0.000001)
        t3 = "It's less than 1 us"
    else
        t3 = string(round((t3_E-t3_S)*10^-9, digits=6))
    end
    

    println(t1)

    println(t2)

    println(t3)

    open("time_response.csv", "w") do io
        write(io, "Linear,Quadratic,Cubic\n")
        write(io, t1,",",t2,",",t3)
    end;
    
    scatter(x, y, markersize=10,label="Data points")
    #plot!(x_new, fx(x_new), w=3,label="Real Data", reuse=false) # real function graph
    
    plot!(x_new, f_linear(x_new), w=3,label="Linear interpolation", reuse=false)
    plot!(x_new, f_quadratic(x_new), linestyle=:dash, w=3, label="Quadratic interpolation", reuse=false)
    plot!(x_new, f_cubic(x_new), linestyle=:dash, w=3, label="Cubic Spline interpolation", reuse=false)
end

function set_graph(x,y)
    width, height = 640, 480 # width and height of canvas
    plot!(size = (width, height), reuse=false)
    xlims = (-4, 2)
    plot!(legend = :bottomleft, reuse=false)
    current_dir = pwd()*"\\plot_julia.png"
    savefig(current_dir)
    
end
# *********************************************************

function main(start, stop, N)
    x = linspace(start,stop,N)
    x_new = linspace(start,stop,N*10)
    y = fx(x)
    plot_graph(x, y, x_new)
    set_graph(x,y)
end

if abspath(PROGRAM_FILE) == @__FILE__
    start = 1
    stop =  10
    N = 10
    main(start, stop, N)
end
