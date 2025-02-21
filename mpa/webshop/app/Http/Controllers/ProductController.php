<?php

namespace App\Http\Controllers;

use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;
class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('product.product_create');
    }

    /**
     * Store a newly created resource in storage.
     */

    /**
     * Display the specified resource.
     */
    public function show(Product $product)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Product $product)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Product $product)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Product $product)
    {
        //
    }
    public function store(Request $request)
    {
        $validated = Validator::make($request->all(),[
            "name"=>"required|string|min:2|max:20",
            "price"=>"required|decimal:2|numeric|min:0",
            "amount"=>"required|integer|numeric|min:1",
        ], [
            "*.required"=>"de :attribute is verplicht",
            "*.string"=>":attribute moet een tekst zijn",
            "*.min"=>":attribute moet minstens :min zijn",
            "*.max"=>":attribute moet maximum :max zijn",
            "*.numeric"=>":attribute moeten nummers zijn",
            "*.integer"=>":attribute moet een nummer zijn",
            "price.decimal"=>":attribute moet twee nummers achter het heelgetal hebben."

        ])->validate();

        product::create(
            [
                "name" => $request->get("name"),
                "price" => $request->get("price"),
                "amount" => $request->get("amount"),
            ]

        );
        return redirect()->route("overview");
    }
}

