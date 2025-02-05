<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

Route::get('welcome', function () {
    return view('welcome.welcome');
});
Route::get("/hello", [WelcomeController::class, "index"])->name("overview");

Route::get("/product/create", [\App\Http\Controllers\ProductController::class, "create"]);
route::post("/product/store", [\App\Http\Controllers\ProductController::class, "store"]);

require __DIR__.'/auth.php';
