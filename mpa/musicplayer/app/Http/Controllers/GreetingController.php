<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class GreetingController extends Controller
{
    function sayHello(){
        return view("helloworld");
    }
}
