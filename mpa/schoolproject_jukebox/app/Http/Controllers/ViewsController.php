<?php

namespace App\Http\Controllers;

use App\Models\views;
use Illuminate\Http\Request;

class ViewsController extends Controller
{
    public function index()
    {
        return view('index');
    }

    public function hello()
    {
        return view('hello');
    }


    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(views $views)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(views $views)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, views $views)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(views $views)
    {
        //
    }
}