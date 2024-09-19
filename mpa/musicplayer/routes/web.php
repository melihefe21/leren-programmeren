<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\SongController;
use App\Http\Controllers\Welcome;

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

Route::get('/', function () {
    return view('products/index');
});
Route::get("/hello", [welcome::class, "hello"]);
Route::get('/hello', [Welcome::class, 'hello']);
Route::get('/songs', [SongController::class, 'index']);


Route::get("/hello", [ViewsController::class, "hello"])->name('hello');


Route::get('views', function () {
    return view('layout/master');
});

Route::get("/views", [ViewsController::class, "index"]);

Route::get("/playlist/all", [PlaylistController::class,"index"]);
Route::get("/playlist/view/{playlist}", [PlaylistController::class,"show"]);
Route::post("/playlist/addsong/{playlist}", [PlaylistController::class, "AddSongtoPlaylist"]);

require __DIR__.'/auth.php';