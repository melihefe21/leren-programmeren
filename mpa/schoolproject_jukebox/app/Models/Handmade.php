<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Handmade extends Model
{
    use HasFactory;

    public function handmade(){
        return $this->hasMany(Yarn::class);
    }
}
