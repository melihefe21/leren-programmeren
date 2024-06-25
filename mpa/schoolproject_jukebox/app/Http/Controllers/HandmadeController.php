<?php

namespace App\Http\Controllers;

use App\Models\Handmade;
use Illuminate\Http\Request;
class HandmadeController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //view
        $handmade = Handmade::all();
        dd($handmade);
        return view("handmade.index", ["handmade"=> $handmade]);
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
    public function show(Handmade $handmade)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Handmade $handmade)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Handmade $handmade)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Handmade $handmade)
    {
        //
    }
}
